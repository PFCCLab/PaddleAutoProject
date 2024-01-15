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
        'issue_name': "PIR Python API 适配升级",

        # `【黑客松】PIR Python API 适配升级` 任务开始时间，只会统计任务开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2023-10-20T00:00:48Z',

        # 黑客松 issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/58067',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 315,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [68,110],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["PIR Python API 适配升级"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-315']],
        
        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PIR API adaptor No.",
        
        # PR、状态等信息所在的列
        'pr_col': 3,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Docathon】补充缺失的中文 API 文档",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2023-09-15T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/docs/issues/6193',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 最大的任务ID
        'max_task_id' : 67,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [], 

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Docathon"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-67']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Add CN Doc No.",

        # PR、状态等信息所在的列
        'pr_col': 4,
    },{
        # 任务名称，起标识作用
        'issue_name': "【PIR】 PIR下的OP单测修复",

        # 【PIR】 PIR下的OP单测修复 任务开始时间
        'start_time' : '2023-11-28T00:00:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/59382',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 39,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["快乐开源"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-39']],
        
        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PIR OpTest Fix No.",
        
        # PR、状态等信息所在的列
        'pr_col': 3,
    },{
        # 任务名称，起标识作用
        'issue_name': "【快乐开源】API 文档补全",

        # 【快乐开源】API 文档补全 任务开始时间
        'start_time' : '2023-12-08T00:00:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleScience/issues/686',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleScience/pulls'],

        # 最大的任务ID
        'max_task_id' : 109,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["快乐开源"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-109']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PPSCI Doc No.",

        # PR、状态等信息所在的列
        'pr_col': 3,
    },{
        # 任务名称，起标识作用
        'issue_name': "【PIR】PIR下的分布式算子注册",

        # 【PIR】 PIR下的OP单测修复 任务开始时间
        'start_time' : '2023-12-28T00:00:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/60436',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 30,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["快乐开源"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-30']],
        
        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PIR Dist Op Reg No.",
        
        # PR、状态等信息所在的列
        'pr_col': 3,
    },{
        # 任务名称，起标识作用
        'issue_name': "【快乐开源】paddle_test推全",

        # 【快乐开源】API 文档补全 任务开始时间
        'start_time' : '2024-01-15T00:00:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://github.com/PaddlePaddle/Paddle/issues/60793',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 43,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["快乐开源"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-43']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "paddle_test No.",

        # PR、状态等信息所在的列
        'pr_col': 3,
    },
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
