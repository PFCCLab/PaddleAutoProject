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
        'issue_name': "【快乐开源】为 PaddleScience 案例添加 export 和 inference 功能",

        # 【快乐开源】为 PaddleScience 案例添加 export 和 inference 功能
        'start_time' : '2024-02-26T00:00:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleScience/issues/788',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleScience/pulls'],

        # 最大的任务ID
        'max_task_id' : 35,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["快乐开源"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-35']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PPSCI Export&Infer No.",

        # PR、状态等信息所在的列
        'pr_col': 4,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Hackathon 8th】开源贡献个人挑战赛",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-12-01T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/71310',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleScience/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleNLP/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleMIX/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleYOLO/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleDetection/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleOCR/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleSpeech/pulls',
                      'https://api.github.com/repos/PaddlePaddle/docs/pulls',
                      'https://api.github.com/repos/PaddlePaddle/community/pulls'],

        # 最大的任务ID
        'max_task_id' : 42,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : [“框架开发任务”,"科学计算论文复现任务","套件开发任务"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-4'],['10-27'],
                        [5, 6, 7, 8, 9, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 8th No.",

        # PR、状态等信息所在的列
        'pr_col': 4,
        
        # 如果需要标识完成人，需要写上完成人所在的列
        'complete_col': 5,

        # 是否展示看板信息
        'board': True,

        # 是否为黑客松任务
        'hackathon': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Hackathon 8th】Fundable Projects",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-02-27T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/71311',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id' : 4,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [['1-2']],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : [["Fundable Projects"]],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-4']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "",

        # PR、状态等信息所在的列
        'pr_col': 4,
        
        # 是否展示看板信息
        'board': False,

        # 是否为黑客松任务
        'hackathon': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 8th Code Camp】黑客松护航计划集训营（正式批）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-02-27T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/71312',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id' : 5,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [['3']],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : [["护航计划集训营（正式批）"]],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-5']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "",

        # PR、状态等信息所在的列
        'pr_col': 5,
        
        # 是否展示看板信息
        'board': False,

        # 是否为黑客松任务
        'hackathon': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 8th Code Camp】飞桨正式实习招聘（可在校）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-02-27T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/71313',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id' : 1,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : [["飞桨正式实习招聘"]],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "",

        # PR、状态等信息所在的列
        'pr_col': 5,
        
        # 是否展示看板信息
        'board': False,

        # 是否为黑客松任务
        'hackathon': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "PaddleMIX 快乐开源活动 (2025 H1)",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-3-10T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleMIX/issues/1046',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleMIX/pulls'],

        # 最大的任务ID
        'max_task_id' : 29,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["飞桨多模态大模型快乐开源活动"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-29']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PPMix No",

        # PR、状态等信息所在的列
        'pr_col': 7,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【紧急召集】Paddle主框架文档修复任务，速来！",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-02-20T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/71203',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls', 'https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 最大的任务ID
        'max_task_id' : 20,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Paddle主框架文档提升"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-20']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Update Doc No",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "PaddleNLP 快乐开源活动 (2025 H1)",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-03-10T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleNLP/issues/9763',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleNLP/pulls'],

        # 最大的任务ID
        'max_task_id' : 35,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["飞桨大语言模型快乐开源活动"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-35']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PaddleNLP No.",

        # PR、状态等信息所在的列
        'pr_col': 7,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "PaddleSpeech 快乐开源活动 (2025 H1)",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-02-28T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleSpeech/issues/3997',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleSpeech/pulls'],

        # 最大的任务ID
        'max_task_id' : 15,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["PaddleSpeech 快乐开源活动"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-15']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PaddleSpeech No.",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': True,
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
