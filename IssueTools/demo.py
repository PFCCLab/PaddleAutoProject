import os
from config_infor import *


raw = os.popen(f'curl \
                --request GET \
                --url "https://api.github.com/repos/PaddlePaddle/Paddle/issues/{PR_ID}" \
                --header "Accept: application/vnd.github+json" \
                --header "Authorization: Bearer {TOKENS}"')
msg = raw.buffer.read().decode('utf-8')

with open('test.txt','w') as f:
    for line in msg:
        f.write(line)