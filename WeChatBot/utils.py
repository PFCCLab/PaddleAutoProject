import os
from config_infor import *
import json
import datetime

def get_issue_user_open(username,token = TOKENS):
    # 获取某账户当前的open issue
    f_string = f'curl \
                --request GET \
                --url "https://api.github.com/repos/PaddlePaddle/Paddle/issues?state=open&creator={username}" \
                --header "Accept: application/vnd.github+json" \
                --header "Authorization: Bearer {token}"'
    raw = os.popen(f_string)
    msg = raw.buffer.read().decode('utf-8')

    data = json.loads(msg)
    pr_num = len(data)
    result_string = username+'的活跃PR数为'+str(pr_num)+'\n'
    for item in data:
        result_string += (str(item['number'])+' '+item['title']+'\n')

    return result_string

def get_issue_user_today(username, token = TOKENS):
    now_time = datetime.datetime.now()
    now_time = datetime.datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0, 0)
    utc_time = now_time - datetime.timedelta(hours=8)  # UTC只是比北京时间提前了8个小时
    utc_time = utc_time.isoformat()
    print(utc_time)

    f_string = f'curl \
                --request GET \
                --url "https://api.github.com/repos/PaddlePaddle/Paddle/issues?state=all&creator={username}&since={utc_time}" \
                --header "Accept: application/vnd.github+json" \
                --header "Authorization: Bearer {token}"'
    raw = os.popen(f_string)
    msg = raw.buffer.read().decode('utf-8')

    data = json.loads(msg)
    pr_num = len(data)
    result_string = username+'的今日PR数为'+str(pr_num)+'\n'
    for item in data:
        result_string += (str(item['number'])+' '+item['title']+" "+item['state']+'\n')

    if pr_num == 0:
        result_string += "有点不太努力了！\n"
    if pr_num>=3:
        result_string += "真的好卷！\n"

    return result_string

def get_issue(issue_id, token = TOKENS):
    f_string = f'curl \
                --request GET \
                --url "https://api.github.com/repos/PaddlePaddle/Paddle/issues/{PR_ID}" \
                --header "Accept: application/vnd.github+json" \
                --header "Authorization: Bearer {TOKENS}"'