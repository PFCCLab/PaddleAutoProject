import os
from config_infor import *
import json

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

def get_issue(issue_id, token = TOKENS):
    f_string = f'curl \
                --request GET \
                --url "https://api.github.com/repos/PaddlePaddle/Paddle/issues/{PR_ID}" \
                --header "Accept: application/vnd.github+json" \
                --header "Authorization: Bearer {TOKENS}"'