# -*- coding: utf-8 -*-
import logging
import os
import json

common_config = {
    # 更新issue的token
    'issue_token': os.environ.get('ISSUE_TOKEN'),

    # 更新评论的token
    'comment_token': os.environ.get('COMMENT_TOKEN'),

    # 代理地址
    'proxies': {
        'http': os.environ.get('HTTP_PROXY'),
        'https': os.environ.get('HTTPS_PROXY')
    },

    # 是否展示看板信息
    'board': True,

    'comment_to_user_list': []
}

configs = [
    {
        # 任务名称，起标识作用
        'issue_name': "PaddleMIX 快乐开源活动 (2025 H1)",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-03-10T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleMIX/issues/1046',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleMIX/pulls'],

        # 最大的任务ID
        'max_task_id' : 30,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["飞桨多模态大模型快乐开源活动"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-30']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PPMix No",

        # PR、状态等信息所在的列
        'pr_col': 7,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【开源任务】Paddle CPU/GPU Kernel 精度问题推全",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-05-12T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/72667',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls','https://api.github.com/repos/PFCCLab/PaddleAPITest/pulls'],

        # 最大的任务ID
        'max_task_id' : 183,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["精度问题修复"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-183']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Accuracy diff No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': True,

        # 是否为黑客松任务
        'hackathon': False,
    }
]


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
