import time
import json
import schedule

import utils
from config import config, logger


def update_issue_automatically():

    try:
        issue_url = config['issue_url']
    
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
        repo_urls = config['repo_urls']

        for repo_url in repo_urls:
            params = {
                "state": "open"
            }
            pulls = utils.request_get_multi(repo_url, params)
            for pull in pulls:
                if pull['created_at'] > config['start_time']:
                    utils.update_status_by_pull(task_list, pull)

            params = {
                "state": "closed"
            }
            pulls = utils.request_get_multi(repo_url, params)
            for pull in pulls:
                if pull['created_at'] > config['start_time'] and pull['merged_at']:
                    utils.update_status_by_pull(task_list, pull)


        # 4. 更新榜单内容
        updated_issue = response['body']
        for task in task_list:
            if task == None:
                continue
            num = int(task['num'].strip(' '))
            start = updated_issue.find('| {} |'.format(num))
            end = start + 1
            while end < len(updated_issue) and updated_issue[end] != '\r' and updated_issue[end] != '\n':
                end += 1
            
            # TODO：这里后期需要定制化表头
            row = '| {} | {} | {} | {} | {} |'.format(num, task['difficulty'], task['issue'], task['status'], task['team'])
            updated_issue = f'{updated_issue[:start]}{row}{updated_issue[end:]}'
        
        
        if config["hackathon"]:
            # 5. 更新看板信息，框架计划不需要更新看板信息
            board_info = utils.update_board(task_list)
            start = updated_issue.find('看板信息')
            while updated_issue[start] != '\n':
                start += 1
            end = updated_issue.find('#####', start)
            updated_issue = updated_issue[: start + 1] + board_info + updated_issue[end:]

        # 6. 处理换行符，写入日志存档
        updated_issue = updated_issue.replace('\r', '')
        file_name = time.strftime('%Y-%m-%dT%H-%M-%S', time.localtime())
        with open('./logs/{}.md'.format(file_name), mode='w', encoding='utf-8') as f:
            f.write(updated_issue)

        # 7. 更新 issue
        data = {}
        data['body'] = updated_issue
        data['title'] = response['title']

        res = utils.request_update_issue(issue_url, json.dumps(data))
        # logger.info('更新issue内容返回结果: ' + str(res))
        print(res)

    except Exception as e:
        logger.exception(e)

    


if __name__ == '__main__':

    # 运行一次查看效果
    update_issue_automatically()

    # 每两小时运行一次
    schedule.every(2).hours.do(update_issue_automatically)

    while True:
        try:
            schedule.run_pending()
            time.sleep(100)
        except Exception as e:
            logger.error(e)