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
        'issue_name': "【Docathon】补充Overview文档相关API描述",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2024-02-01T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/docs/issues/6427',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 最大的任务ID
        'max_task_id': 36,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["Docathon"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types': [['1-36']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix': "Add Overview Doc No.",

        # PR、状态等信息所在的列
        'pr_col': 4,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Docathon】为 Tensor API 文档增加图例",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2024-04-17T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/docs/issues/6614',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 最大的任务ID
        'max_task_id': 60,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["Docathon"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types': [['1-60']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix': "Add API Legend No.",

        # PR、状态等信息所在的列
        'pr_col': 4,
    },{
        # 任务名称，起标识作用
        'issue_name': "【快乐开源】报错日志体系优化 ",

        # 【PIR】 PIR下的OP单测修复 任务开始时间
        'start_time' : '2023-03-15T00:00:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/62748',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

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
        'pr_prefix' : "Error Message No. ",

        # PR、状态等信息所在的列
        'pr_col': 3,
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
        'issue_name': "【complex op】paddlepaddle 支持复数",

        # 【complex op】paddlepaddle 支持复数 任务开始时间
        'start_time' : '2023-08-10T00:00:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/61975',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 55,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["快乐开源"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-55']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "complex op No.",

        # PR、状态等信息所在的列
        'pr_col': 3,
    }, {
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
        'issue_name': "【Hackathon 6th】开源贡献个人挑战赛",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-03-21T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/62905',

        # 监控的仓库列表
        'repo_urls':  ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls',
             'https://api.github.com/repos/PaddlePaddle/community/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleScience/pulls',
             'https://api.github.com/repos/PaddlePaddle/Paddle2ONNX/pulls',
             'https://api.github.com/repos/openvinotoolkit/openvino/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaConvert/pulls',
             'https://api.github.com/repos/PaddlePaddle/docs/pulls',
            ],

        # 最大的任务ID
        'max_task_id' : 55,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [46],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["框架 API 开发任务", "框架分布式开发任务", "框架其他开发任务", "科学计算模型复现任务","合作伙伴任务"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-32'],
                        ['33-35'],
                        ['50-55'],
                        ['36-42'],
                        ['43-49']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 6th No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 如果需要标识完成人，需要写上完成人所在的列
        'complete_col': 5,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Hackathon 6th Code Camp】飞桨护航计划集训营（第二批）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-03-21T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/62906',

        # 监控的仓库列表
        'repo_urls':  [],

        # 最大的任务ID
        'max_task_id' : 4,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["飞桨护航计划集训营（第二批）"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-4']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "",

        # PR、状态等信息所在的列
        'pr_col': 5,

        # 是否展示看板信息
        'board': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Hackathon 6th】优秀稿件征集与传播",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-03-21T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/62907',

        # 监控的仓库列表
        'repo_urls':  ['https://api.github.com/repos/PaddlePaddle/community/pulls'],

        # 最大的任务ID
        'max_task_id' : 7,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["优秀稿件征集与传播"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-7']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 6th Article No.",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 如果需要标识完成人，需要写上完成人所在的列
        'complete_col': 4,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Hackathon 6th】Fundable Projects",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-03-21T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/62908',

        # 监控的仓库列表
        'repo_urls':  [],

        # 最大的任务ID
        'max_task_id' : 6,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Fundable Projects"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-6']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 6th Fundable Projects No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "Fundable Projects No.3 修改算子列表",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-04-01T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/63303',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 397,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Fundable Projects No.3"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-397']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 6th Fundable Projects 3 No.",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "[docs清理] 清理未暴露在 sphinx toctree 下的文档",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-04-09T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/docs/issues/6491',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 最大的任务ID
        'max_task_id' : 58,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Docathon"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-58']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Remove File No.",

        # PR、状态等信息所在的列
        'pr_col': 3,

    },{
        # 任务名称，起标识作用
        'issue_name': "【疑难解决】解决PaddleOCR历史存在的疑难Issue",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-04-09T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleOCR/issues/11906',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleOCR/pulls'],

        # 最大的任务ID
        'max_task_id' : 10,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Fundable Projects No.3"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-10']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "OCR Issue No.",

        # PR、状态等信息所在的列
        'pr_col': 5,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Hackathon 6th Fundable Projects No.4】Paddle 框架旧执行器功能退场 Tracking Issue",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-03-30T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/63510',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls','https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 最大的任务ID
        'max_task_id' : 6,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Fundable Projects No.4"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-6']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 6th Fundable Projects 4 No.",

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
