import time
import json
import schedule

import utils


def update_issue_automatically():
    # 1. 获取issue表格
    response = utils.request_get_issue(issue_url)

    # 从issue中提取题目列表
    task_list = utils.process_issue(response['body'])

    # 2. 根据评论更新表格
    comment_url = issue_url + '/comments'
    comments = utils.request_get_multi(comment_url)
    for comment in comments:
        utils.update_status_by_comment(task_list, comment)
        

    # 3. 根据PR更新表格
    # - 根据提出的PR更新状态为已提交
    # - 根据close的PR更新状态为已完成

    # TODO：这里可以改变监测的仓库
    repo_urls = ['https://api.github.com/repos/Tomoko-hjf/paddleviz/pulls']

    for repo_url in repo_urls:
        params = {
            "state": "open"
        }
        pulls = utils.request_get_multi(repo_url, params)
        for pull in pulls:
            utils.update_status_by_pull(task_list, pull)

        params = {
            "state": "closed"
        }
        pulls = utils.request_get_multi(repo_url, params)
        for pull in pulls:
            if pull['merged_at']:
                utils.update_status_by_pull(task_list, pull)


    # 4. 更新榜单内容
    updated_issue = response['body']
    for task in task_list:
        num = int(task['num'].strip(' '))
        start = updated_issue.find('| {} |'.format(num))
        end = start + 1
        while end < len(updated_issue) and updated_issue[end] != '\r' and updated_issue[end] != '\n':
            end += 1
        
        # TODO：这里后期需要定制化表头
        row = '| {} | {} | {} | {} | {} |'.format(num, task['difficulty'], task['issue'], task['status'], task['team'])
        updated_issue = f'{updated_issue[:start]}{row}{updated_issue[end:]}'
    
    # 处理换行符
    updated_issue = updated_issue.replace('\r', '')
    file_name = time.strftime('%Y-%m-%dT%H-%M-%S', time.localtime())
    with open('./logs/{}.md'.format(file_name), mode='w', encoding='utf-8') as f:
        f.write(updated_issue)

    # 5. 更新 issue
    data = {}
    data['body'] = updated_issue
    data['title'] = response['title']
    data['assignee'] = response['assignee']
    data['state'] = response['state']
    data['state_reason'] = response['state_reason']
    data['milestone'] = response['milestone']
    data['labels'] = response['labels']

    res = utils.request_update_issue(issue_url, json.dumps(data))

    # 5. 更新看板信息
    utils.update_board(task_list)
    # start = updated_issue.find("看板")
    # start = updated_issue.find("<img", start)
    # end = updated_issue.find(">", start)
    # updated_issue = updated_issue[: start] + "<img src=data:image/jpg;base64,{} />".format(board) + updated_issue[end + 1:]



if __name__ == '__main__':
    
    # issue链接
    issue_url = 'https://api.github.com/repos/Tomoko-hjf/paddleviz/issues/1'

    # 运行一次查看效果
    update_issue_automatically()

    # 每两小时运行一次
    schedule.every(2).hours.do(update_issue_automatically)

    while True:
        schedule.run_pending()
        time.sleep(10)