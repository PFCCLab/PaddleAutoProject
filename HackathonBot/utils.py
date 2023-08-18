import base64
import os

import requests
import time
import logging
import imgkit

access_token = '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'
headers = {'Authorization': f'token {access_token}', 'Accept': 'application/vnd.github.raw+json', 'X-GitHub-Api-Version': '2022-11-28'}
proxies={
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

# 总的任务数量
task_num = 200

# 黑客松开始时间，只会统计黑客松开始时间之后的PR
startTime = '2023-07-28T13:33:48Z'

# TODO：这里需要定制化表头
column_name = ['num', 'difficulty', 'issue', 'status', 'team']

# 忽略不处理的题号，这部分留给人工处理
un_handle_tasks = []

# TODO: 需要写明每个赛道所包含的赛题，每个赛道是一个数组
task_types = [[1, 2],
              [3, 4]]
type_names = ["API开发", "算子性能优化"]

def request_get_issue(url, params={}):
    """
    @desc: 返回单条issue
    """
    response = requests.get(url, headers=headers, proxies=proxies, params=params)
    response = response.json()
    return response


def request_get_multi(url, params={}):
    """
    @desc: 根据url获取请求, 将回复转为json格式，注意会返回某个时间之前所有的回复
    """
    # 总的结果汇总
    result = []

    # 模糊查询title （TODO: Rest API 没有提供此功能，可能需要 GraphQL API）
    # params["head"] = "in:title+Hackathon"
    params["per_page"] = 100
    
    # 当前时间
    curTime = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime())
    # 当前请求页
    page = 1

    while curTime > startTime:
        # 请求结果
        params['page'] = page
        response = requests.get(url, headers=headers, proxies=proxies, params=params)
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


def request_update_issue(url, data):
    """
    desc: 更新issue内容

    params:
        url: str 推送的url地址
        data: str 推送的issue内容
    """
    response = requests.patch(url, data=data, headers=headers, proxies=proxies)
    response = response.json()
    return response


def process_issue(task_text):
    """
    desc: 从文本中提取题目列表，并封装为题目对象

    params:
        task_text: str 题目列表文本

    return:
        task_list: [] 对象格式的题目列表，每一列都是对象的一个属性，用字符串表示
    """
    task_list = []
    for i in range(task_num):
        start = task_text.find('| {} |'.format(i + 1))
        # 如果没有找到该编号的任务，直接返回
        if start < 0:
            return task_list
        end = start + 1
        column = 0
        task = {}
        while end < len(task_text) and task_text[end] != '\r' and task_text[end] != '\n':
            if (task_text[end] == '|'):
                item_content = task_text[start + 1: end]
                start = end            
                item_content = item_content.strip(' ')
                task[column_name[column]] = item_content
                column += 1
            end += 1
        task_list.append(task)
    
    return task_list


def update_status_by_comment(tasks, comment):
    """
    desc: 根据评论更新表格内容

    params:
        tasks: 处理后的task对象数组
        comment: 处理后的comment对象

    """
    # 提取评论信息，将字符串格式化为对象
    comment = process_comment(comment)
    
    # 只更新报名信息
    if '报名' not in comment['status']:
        return
    
    # 依次更新评论中提到的每个题目
    if 'num' in comment:
        for num in comment['num']:

            # 对于手工修改的task，无需进行处理
            if num in un_handle_tasks:
                return

            task = tasks[num - 1]
            update_status = {
                'username': comment['username'],
                'status': '报名',
                'pr': []
            }
            task['status'] = get_updated_status(task['status'], update_status)


def update_status_by_pull(tasks, pull):
    """
    @desc: 根据 open issue 更新表格内容
    """
    title = pull['title']
    username = pull['user']['login']
    html_url = pull['html_url']
    state = pull['state']
    if 'Hackathon No.' in title:
        # 获取题目编号
        start = 0
        while title[start] < '0' or title[start] > '9':
            start += 1
        end = start + 1
        while title[end] >= '0' and title[end] <= '9':
            end += 1
        num = int(title[start: end])

        # 防止某些PR编号写错
        if num > len(tasks):
            logging.error('pull编号错误：' + pull['html_url'])
            return
        
        # 对于手工修改的task，无需进行处理
        if num in un_handle_tasks:
            return

        task = tasks[num - 1]

        # TODO：状态需要定制化
        if 'community' in html_url:
            update_status = {
                'username': username,
                'status': '提交RFC' if state == 'open' else '完成设计文档',
                'pr': ['[#{}]({})'.format(html_url[html_url.rfind('/') + 1: ], html_url)]
            }
        else:
            update_status = {
                'username': username,
                'status': '提交PR' if state == 'open' else '完成任务',
                'pr': ['[#{}]({})'.format(html_url[html_url.rfind('/') + 1: ], html_url)]
            }

        task['status'] = get_updated_status(task['status'], update_status)

        # 处理过程中发现已完成任务，则更新完成人信息
        if "完成任务" in task["status"]:
            status = task["status"]
            end = status.find("完成任务")
            start = status.rfind("@", end)
            end = status.find(" ", start)
            task["team"] = status[start: end]
            un_handle_tasks.append(num)


def process_comment(comment):
    """
    @desc: 提取评论信息，将字符串化的status转化为对象信息
    """
    comment_obj = {}
    # 获取评论者的用户名和评论内容
    comment_obj['username'] = comment['user']['login']
    content = comment['body']
    comment_obj['created_at'] = comment['created_at']

    content = content.replace('：',':').replace(',', '、').replace('[','【').replace(']','】')

    # 获取题号
    start = content.find("序号")
    while content[start] < '0' or content[start] > '9':
        start += 1
    end = start + 1
    while content[end] != '\r' and content[end] != '\n':
        end += 1
    
    # TODO: 题号需要用顿号隔开
    nums = content[start: end].strip(' ').split('、')
    nums = [int(num) for num in nums]
    comment_obj['num'] = nums
    
    # 获取状态
    start = content.find("状态") + 2
    end = start + 1
    while content[end] != '\r' and content[end] != '\n':
        end += 1
    comment_obj['status'] = content[start: end].strip(' ')

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
        start = user_status.find('[', start)
        if start != -1:
            prs = user_status[start:]
    
    # 新加入PR(因为返回的PR是倒序返回的，所以需要头插)
    for pr in update_status['pr']:
        if pr not in prs:
            prs = pr + ' ' + prs
    
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
        elif update_status['status'] == '完成任务':
            badge = '<img src="https://img.shields.io/badge/状态-完成任务-9B59B6" />'
    else:
        # 如果不需要变更用户状态，则沿用之前的状态
        if user_status == None:
            badge = ""
        start = user_status.find("<img")
        end = user_status.find("/>")
        if start != -1 and end != -1:
            badge = user_status[start: end + 2]

    
    # 格式化当前用户的状态
    status = '@{} {} {}'.format(update_status['username'], badge, prs)
    
    # 如果该用户存在则替换
    if '@' + update_status['username'] in ori_status:
        start = ori_status.find('@' + update_status['username'])
        end = ori_status.find('<br>')
        ori_status = f'{ori_status[ :start]}{status}{ori_status[end: ]}'
    # 否则追加
    else:
        ori_status += '{}<br>'.format(status)

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
    elif "完成任务" in status:
        status_level = 5
    else:
        status_level = 0

    return status_level


def update_board(tasks):

    board_head = "<!DOCTYPE html> <html> <head><style>table { width: 100%; border-collapse: collapse;} th, td { border: 1px solid black; padding: 8px; text-align: center; } th { background-color: #f2f2f2;} .progress { height: 20px; width: 100%; background-color: #f2f2f2; border: 1px solid #ccc; position: relative;} .progress-inner { height: 100%; width: 0; background-color: #4CAF50;position: absolute; text-align: center; color: white; } </style> <body> <table> <tr> <th>任务方向</th> <th>任务数量</th> <th>提交作品 / 任务认领</th> <th>提交率</th> <th>完成</th> <th>完成率</th> </tr>"

    for i in range(len(task_types)):
        type_name = type_names[i]
        task_num, claimed, submitted, completed = len(task_types[i]), 0, 0, 0
        
        for task_id in task_types[i]:
            task = tasks[task_id - 1]
            status = task["status"]
            if "完成任务" in status:
                completed += 1
                submitted += 1
                claimed += 1
            elif "提交RFC" in status or "完成设计文档" in status or "提交PR" in status:
                submitted += 1
                claimed += 1
            elif "报名" in status:
                claimed += 1
        
        row = '<tr><td>{}</td> <td>{}</td> <td>{} / {}</td> <td>{}%</td> <td>{}</td> <td> <div class="progress"> <div class="progress-inner" style="width: {}%;">{}%</div> </div> </td> </tr>'.format(type_name, task_num, submitted, claimed, round(submitted / task_num * 100, 2), completed, round(completed / task_num * 100, 2), round(completed / task_num * 100, 2))

        board_head += row

    board_head += "</table> </body> </html>"

    options = {'encoding': 'UTF-8' }

    with open("temp.html", mode="w", encoding="utf-8") as f:
        f.write(board_head)
    
    # 如果是Linux系统可以删除这个con或设置为None
    con = imgkit.config(wkhtmltoimage='D:\\Software\\wkhtmltox\\bin\\wkhtmltoimage.exe')
    imgkit.from_file("temp.html", "./image/board.jpg", options=options, config=con)
    
    os.remove("temp.html")

    # 将图片转为base64编码
    # with open("./image/board.jpg", 'rb') as image_file:
    #     encoded_string = base64.b64encode(image_file.read())
    #     encoded_string = encoded_string.decode('utf-8')
    #     print(encoded_string)

    # return encoded_string



