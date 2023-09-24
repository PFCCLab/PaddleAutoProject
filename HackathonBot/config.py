import logging
import os

# 监控的仓库列表
repo_urls = ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls',
             'https://api.github.com/repos/PaddlePaddle/community/pulls',
            ]

config = {
    # 更新issue的token
    'issue_token':  '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', # os.environ.get('ISSUE_TOKEN'),

    # 更新评论的token
    'comment_token': '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', #os.environ.get('COMMENT_TOKEN'),

    # 代理地址
    'proxies': {
        'http': 'http://127.0.0.1:7890', #os.environ.get('HTTP_PROXY'),
        'https': 'http://127.0.0.1:7890', #os.environ.get('HTTPS_PROXY')
    },

    # 黑客松开始时间，只会统计黑客松开始时间之后的PR(注意时间中的字母T和Z不能缺少)
    'start_time' : '2023-09-13T00:28:48Z',

    # 黑客松 issue页面 url 地址, 注意结尾不要有斜杠
    'issue_url': 'https://api.github.com/repos/Tomoko-hjf/paddleviz/issues/7',

    # 监控的仓库列表
    'repo_urls': [],

    # 总的任务数量
    'task_num' : 2,

    # 忽略不处理的题号，这部分留给人工处理
    'un_handle_tasks' : [],

    # 已删除的赛题
    'removed_tasks' : [],

    # 赛道名
    'type_names' : ["热身赛"], 

    # 每个赛题所属的赛道，每个赛道是一个数组
    'task_types' : [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]],

}

def get_logger():
    logger = logging.getLogger('logger')
    logger.setLevel(level=logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    file_handler = logging.FileHandler('./logs/output.txt', encoding='utf-8')
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

logger = get_logger()
