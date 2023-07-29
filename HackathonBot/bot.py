import utils


def update_issue_automatically():
    # 1. 获取issue表格
    response = utils.request_get_issue(issue_url)
    with open('C:/Users/25942/Desktop/test.txt', mode='w', encoding='utf-8') as f:
        f.write(response['body'])

    # 从issue中提取题目列表
    task_list = utils.process_issue(response['body'], task_num)

    # 2. 根据评论更新表格
    comment_url = issue_url + '/comments'
    comments = utils.request_get_multi(comment_url)
    for comment in comments:
        utils.update_status_by_comment(task_list, comment)
    
    with open('./test.txt', mode='w', encoding='utf-8') as f:
        f.write(response['body'])
        

    # 3. 根据PR更新表格
    # - 根据提出的PR更新状态为已提交
    # - 根据close的PR更新状态为已完成
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
    with open('./test1.txt', mode='w', encoding='utf-8') as f:
        f.write(updated_issue)

    # 5. 更新 issue
    res = utils.request_update_issue(issue_url, updated_issue)


if __name__ == '__main__':
    # TODO: 替换为自己的GitHub访问令牌和要获取评论的issue的信息
    owner = 'PaddlePaddle'
    repo = 'Paddle'
    issue_number = '43938'
    task_num = 200
    issue_url = 'https://api.github.com/repos/Tomoko-hjf/paddleviz/issues/1'
    
    update_issue_automatically()