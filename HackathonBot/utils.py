import requests
import time
import json
import re

from config import logger


def request_get_issue(url, params={}, config={}):
    """
    @desc: 返回单条issue
    """
    comment_headers = {'Authorization': f'token {config["comment_token"]}', 'Accept': 'application/vnd.github.raw+json', 'X-GitHub-Api-Version': '2022-11-28'}
    response = requests.get(url, headers=comment_headers, proxies=config["proxies"], params=params)
    response = response.json()
    return response


def request_get_multi(url, params={}, config={}):
    """
    @desc: 根据url获取请求, 将回复转为json格式，注意会返回某个时间之前所有的回复
    """
    comment_headers = {'Authorization': f'token {config["comment_token"]}', 'Accept': 'application/vnd.github.raw+json', 'X-GitHub-Api-Version': '2022-11-28'}
    # 总的结果汇总
    result = []

    # 模糊查询title （TODO: Rest API 没有提供此功能，可能需要 GraphQL API）
    # params["head"] = "in:title+Hackathon"
    params["per_page"] = 100
    
    # 当前时间
    curTime = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime())
    # 当前请求页
    page = 1

    while curTime > config['start_time']:
        # 请求结果
        params['page'] = page
        response = requests.get(url, headers=comment_headers, proxies=config["proxies"], params=params)
        response = response.json()

        # 如果已经没有PR了，直接返回已有的
        if len(response) == 0:
            return result
        
        # 合并结果
        result.extend(response)
        
        # 更新当前时间和请求页 
        curTime = response[-1]['created_at']
        page += 1
    
    return result


def comment_to_user(data, config):
    """
    desc: 在issue下回复（报名格式、编号错误， pr 编号错误）

    params:
        data: comment 内容
    """
    comment_headers = {'Authorization': f'token {config["comment_token"]}', 'Accept': 'application/vnd.github.raw+json', 'X-GitHub-Api-Version': '2022-11-28'}

    # 如果已经回复过了，不再回复
    if data['id'] in config["comment_to_user_list"]:
        return
    data = json.dumps(data)
    response = requests.post(config['issue_url'] + '/comments', data=data, headers=comment_headers, proxies=config["proxies"])
    response = response.json()
    return response


def request_update_issue(url, data, config):
    """
    desc: 更新issue内容

    params:
        url: str 推送的url地址
        data: str 推送的issue内容
    """
    issue_headers = {'Authorization': f'token {config["issue_token"]}', 'Accept': 'application/vnd.github.raw+json', 'X-GitHub-Api-Version': '2022-11-28'}

    response = requests.patch(url, data=data, headers=issue_headers, proxies=config["proxies"])
    response = response.json()
    return response


def process_issue(task_text, config):
    """
    desc: 从文本中提取题目列表，并封装为题目对象

    params:
        task_text: str 题目列表文本

    return:
        task_list: [] 对象格式的题目列表，每一列都是对象的一个属性，用字符串表示
    """
    task_list = []
    for i in range(config['task_num']):
        start = task_text.find('| {} |'.format(i + 1))
        # 如果没有找到该编号的任务，直接返回
        if start < 0:
            logger.info('没有从issue内容中找到编号为【{}】的赛题'.format(str(i + 1)))
            task_list.append(None)
            continue
        end = start + 1
        column = 0
        task = {}
        while end < len(task_text) and task_text[end] != '\r' and task_text[end] != '\n':
            if (task_text[end] == '|'):
                item_content = task_text[start + 1: end]
                start = end            
                item_content = item_content.strip(' ')
                task["col_" + str(column)] = item_content
                column += 1
            end += 1
        task_list.append(task)
    
    return task_list


def update_status_by_comment(tasks, comment, config):
    """
    desc: 根据评论更新表格内容

    params:
        tasks: 处理后的task对象数组
        comment: 处理后的comment对象

    """
    try:
        # 提取评论信息，将字符串格式化为对象
        comment = process_comment(comment, config)

        if comment == None:
            return
        
        # 依次更新评论中提到的每个题目
        if 'num' in comment:
            for num in comment['num']:
                
                # 如果报名的赛题编号错误
                if num > len(tasks) or num <= 0:
                    comment_to_user({"body": "@{} 报名赛题编号【{}】不存在".format(comment['username'], num), "id": "comment-" + str(comment["id"])})
                    config["comment_to_user_list"].append('comment-' + str(comment["id"]))
                    logger.error('@{} 报名赛题编号【{}】不存在：'.format(comment['username'], str(num)))
                    return
                    
                # 对于手工修改的task，无需进行处理
                if num in config['un_handle_tasks']:
                    return
                
                # 对于删除的赛题，需要进行提醒赛题已删除
                if num in config['removed_tasks']:
                    logger.error('@{} 报名的赛题【{}】已被删除'.format(comment['username'], str(num)))
                    comment_to_user({"body": "@{} 抱歉，赛题【{}】已删除".format(comment['username'], num), "id": 'comment-' + str(comment["id"])})
                    config["comment_to_user_list"].append('comment-' + str(comment["id"]))
                    return

                task = tasks[num - 1]

                if task == None:
                    logger.error('赛题【{}】没有出现在任务列表中'.format(num))
                    return

                update_status = {
                    'username': comment['username'],
                    'status': '报名',
                    'pr': []
                }
                state_col = "col_" + str(config["pr_col"] - 1)
                task[state_col] = get_updated_status(task[state_col], update_status)
    except Exception as e:
        logger.error("处理用户【{}】评论出现异常，请检查是否为格式问题, 评论内容为【{}】".format(comment['user']['login'], comment['body']))
        logger.exception(e)

def update_status_by_pull(tasks, pull, config):
    """
    @desc: 根据 open issue 更新表格内容
    """
    title = pull['title']
    username = pull['user']['login']
    html_url = pull['html_url']
    state = pull['state']
    if re.match('.*?{}.*?'.format(config["pr_prefix"]), title) is not None: 
        part_pr = False
        lower_title = title.lower().replace(' ', '')
        if '-part' in lower_title:
            part_pr = True

        # 获取题目编号
        start = title.find('No')
        while title[start] < '0' or title[start] > '9':
            start += 1
        end = start + 1
        while title[end] >= '0' and title[end] <= '9':
            end += 1
        num = int(title[start: end])

        # 防止某些PR编号写错
        if num > len(tasks) or num <= 0:
            comment_to_user({"body": "@{} PR赛题编号【{}】不存在".format(username, num), "id": 'pull-' + str(pull["id"])})
            config["comment_to_user_list"].append('pull-' + str(pull["id"]))
            logger.error('@{} PR #{}中赛题编号【{}】不存在：'.format(username, pull['html_url'], str(num)))
            return
        
        # 对于手工修改的task，无需进行处理
        if num in config['un_handle_tasks']:
            return

        task = tasks[num - 1]

        if task == None:
            logger.error('赛题【{}】没有出现在任务列表中'.format(num))
            return

        if 'community' in html_url:
            update_status = {
                'username': username,
                'status': '提交RFC' if state == 'open' else '完成设计文档',
                'pr': ['[#{}]({})'.format(html_url[html_url.rfind('/') + 1: ], html_url)]
            }
        else:
            status = ''
            if state == 'open':
                status = '提交PR'
            elif part_pr:
                status = '部分完成'
            else:
                status = '完成任务'
            
            update_status = {
                'username': username,
                'status': status,
                'pr': ['[#{}]({})'.format(html_url[html_url.rfind('/') + 1: ], html_url)]
            }
        
        state_col = "col_" + str(config["pr_col"] - 1)
        task[state_col] = get_updated_status(task[state_col], update_status)

        # 处理过程中发现已完成任务，则更新完成人信息
        if "complete_col" in config and "完成任务" in task[state_col]:
            complete_col = "col_" + str(config["complete_col"] - 1)
            task[complete_col] = '@' + username
            config["un_handle_tasks"].append(num)


def process_comment(comment, config):
    """
    @desc: 提取评论信息，将字符串化的status转化为对象信息
    """
    if comment['user']['login'] == 'HackathonBot':
        return None

    comment_obj = {}
    # 获取评论者的用户名和评论内容
    comment_obj['username'] = comment['user']['login']
    content = comment['body']
    comment_obj['created_at'] = comment['created_at']
    comment_obj['id'] = comment['id']

    content = content.replace('：',':').replace('，', ',').replace(',', '、').replace('[','【').replace(']','】')

    # 只更新报名信息
    if '报名:' in content and '【报名】:' not in content:
        logger.error('@{} 报名的格式不正确'.format(comment_obj['username']))
        # comment_to_user({"body": "@{} 请检查报名格式，正确的格式为【报名】: 题目编号".format(comment_obj['username']), "id": 'comment-' + str(comment["id"])})
        config["comment_to_user_list"].append('comment-' + str(comment["id"]))
        return None

    # 获取题号
    start = content.find("【报名】")
    # 不是报名评论，直接返回None
    if start == -1:
        return None

    while start < len(content) and (content[start] < '0' or content[start] > '9'):
        start += 1
    end = start + 1
    while end < len(content) and content[end] != '\r' and content[end] != '\n':
        end += 1
    
    # 题号用顿号隔开或-隔开
    sequence = content[start: end].strip(' ')
    ids = []
    nums = sequence.split('、')
    for num in nums:
        if '-' in num:
            arr = num.split('-')
            arr = [i for i in range(int(arr[0]), int(arr[1]) + 1)]
            ids.extend(arr)
        else:
            ids.append(int(num))
    nums = ids
    
    comment_obj['num'] = nums

    logger.info('{} 报名赛题 {}'.format(comment_obj['username'], str(nums)))

    return comment_obj


def get_updated_status(ori_status, update_status):
    """
    @desc: 根据表格原先的状态信息更新状态，姓名，状态（报名状态、提交RFC、完成设计文档、提交PR、锁定任务、完成任务），PR
        * 注意：不同用户的状态通过<br>分隔
    
    params:
        ori_status: str 原先状态栏的字符串表示
        update_status: dict 更新状态的对象表示，该对象包含 username:str 用户名; status:str 变更后状态；pr:dict pr列表
    """
    # 寻找之前的PR
    prs = ''
    user_status = None

    # 如果用户出现在状态列表中，则需要保留之前的PR
    if update_status['username'] in ori_status:
        start = ori_status.find(update_status['username'])
        end = ori_status.find('<br>', start)
        user_status = ori_status[start: end].strip(' ')
        start = user_status.find('[')
        if start != -1:
            prs = user_status[start:]
    
    # 新加入PR
    for pr in update_status['pr']:
        if pr not in prs:
            prs = prs + ' ' + pr
    
    # 更新状态前需要判断是否可以更新，状态级别只能增大，不能减小
    ori_status_level = get_status_level(user_status)
    update_status_level = get_status_level(update_status["status"])

    if ori_status_level < update_status_level:
        # TODO：状态需要定制化
        if update_status['status'] == '报名':
            badge = '<img src="https://img.shields.io/badge/状态-报名-2ECC71" />'
        elif update_status['status'] == '提交RFC':
            badge = '<img src="https://img.shields.io/badge/状态-提交RFC-F1C40F" />'
        elif update_status['status'] == '完成设计文档':
            badge = '<img src="https://img.shields.io/badge/状态-完成设计文档-3498DB" />'
        elif update_status['status'] == '提交PR':
            badge = '<img src="https://img.shields.io/badge/状态-提交PR-F39C12" />'
        elif update_status['status'] == '部分完成':
            badge = '<img src="https://img.shields.io/badge/状态-部分完成-FFC0CB" />'
        elif update_status['status'] == '完成任务':
            badge = '<img src="https://img.shields.io/badge/状态-完成任务-9B59B6" />'
    else:
        # 如果不需要变更用户状态，则沿用之前的状态
        if user_status == None:
            badge = ""
        else:
            start = user_status.find("<img")
            end = user_status.find("/>")
            if start != -1 and end != -1:
                badge = user_status[start: end + 2]

    
    # 格式化当前用户的状态
    status = '@{} {} {}'.format(update_status['username'], badge, prs)
    
    # 如果该用户存在则替换
    if '@' + update_status['username'] in ori_status:
        start = ori_status.find('@' + update_status['username'])
        end = ori_status.find('<br>', start)
        ori_status = f'{ori_status[ :start]}{status}{ori_status[end: ]}'
    # 否则追加
    else:
        ori_status += '{}<br> '.format(status)

    return ori_status


def get_status_level(status):

    """
    desc: 根据字符串形式的状态获取数字形式的状态编号
    
    params:
        status: str 文本形式的状态

    return:
        status_level: int 数字形式的状态
    """

    if status == None:
        return 0

    if "报名" in status:
        status_level = 1
    elif "提交RFC" in status:
        status_level = 2
    elif "完成设计文档" in status:
        status_level = 3
    elif "提交PR" in status:
        status_level = 4
    elif "部分完成" in status:
        status_level = 5
    elif "完成任务" in status:
        status_level = 6
    else:
        status_level = 0

    return status_level


def update_board(tasks, config):
    """
    desc: 根据任务对象列表获取看板信息

    params:
        tasks: 任务列表对象
    """

    board_head = "| 任务方向 | 任务数量 | 提交作品 / 任务认领 | 提交率 | 完成 | 完成率 |\n| :----: | :----: | :----:  | :----: | :----: | :----: |\n"

    for i in range(len(config['task_types'])):
        type_name = config['type_names'][i]
        task_num, claimed, submitted, completed = 0, 0, 0, 0
        
        for task_range in config['task_types'][i]:
            task_ids = []
            if '-' in str(task_range):
                nums = task_range.split('-')
                task_ids = [i for i in range(int(nums[0]), int(nums[1]) + 1)]
            else:
                task_ids = [int(task_range)]
            
            task_num += len(task_ids)
            
            for task_id in task_ids:
                if task_id > len(tasks):
                    continue
                task = tasks[task_id - 1]
                if task == None:
                    continue
                state_col = "col_" + str(config["pr_col"] - 1)
                status = task[state_col]
                if "完成任务" in status:
                    completed += 1
                    submitted += 1
                    claimed += 1
                elif "提交PR" in status:
                    submitted += 1
                    claimed += 1
                elif "提交RFC" in status or "完成设计文档" in status or "报名" in status:
                    claimed += 1
        
        row = '| {} | {} | {} / {} | {}% | {} | {}% |\n'.format(type_name, task_num, submitted, claimed, round(submitted / task_num * 100, 2), completed, round(completed / task_num * 100, 2), round(completed / task_num * 100, 2))

        board_head += row

    return board_head
