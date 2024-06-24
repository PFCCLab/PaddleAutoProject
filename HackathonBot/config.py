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
        'max_task_id' : 58,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [46, 48, 49, 51],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["框架 API 开发任务", "框架分布式开发任务", "框架其他开发任务", "科学计算模型复现任务","合作伙伴任务","Paddle2ONNX任务"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-32'],
                        ['33-35'],
                        ['50-55'],
                        ['36-42'],
                        ['43-49'],
                        ['56-58']],

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
        'max_task_id' : 12,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Fundable Projects No.6"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-12']],

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
    },{
        # 任务名称，起标识作用
        'issue_name': "【快乐开源】PIR模式下单测问题修复与适配",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-04-26T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/63740',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls','https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 最大的任务ID
        'max_task_id' : 664,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["【快乐开源】PIR模式下单测问题修复与适配"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-664']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Fix PIR Unittest No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "引入 clang-tidy Tracking Issue",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-04-15T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/64128',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 299,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Fundable Projects No.2"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-299']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 6th Fundable Projects 2 No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【快乐开源】PIR下Sparse算子Python API 适配",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-05-22T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/64492',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 14,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["【快乐开源】PIR下Sparse算子Python API 适配"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-14']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Migrate Sparse API No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【问题解决】解决PaddleSpeech历史问题和BUG",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2024-05-24T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleSpeech/issues/3771',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleSpeech/pulls'],

        # 最大的任务ID
        'max_task_id': 12,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["【问题解决】解决PaddleSpeech历史问题和BUG"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types': [['1-12']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix': "Fix Speech Issue No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【问题解决】待提测和待修复的命令和目录",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2024-05-24T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleSpeech/issues/3783',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleSpeech/pulls'],

        # 最大的任务ID
        'max_task_id': 20,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["已验证可提测","待修复"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types': [['1-20']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix': "Speech Demo 2.6.1 No.",

        # PR、状态等信息所在的列
        'pr_col': 5,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【问题解决】Paddlespeech develop版本待提测和待修复的命令和目录",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2024-06-04T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleSpeech/issues/3787',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleSpeech/pulls'],

        # 最大的任务ID
        'max_task_id': 21,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["已验证可提测","待修复"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types': [['1-21']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix': "Speech Demo develop No.",

        # PR、状态等信息所在的列
        'pr_col': 5,

        # 是否展示看板信息
        'board': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 7th Code Camp】黑客松护航计划集训营（提前批）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-06-19T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/65285',

        # 监控的仓库列表
        'repo_urls':  [],

        # 最大的任务ID
        'max_task_id' : 10,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["第七期黑客松护航计划集训营（提前批）"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-10']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "",

        # PR、状态等信息所在的列
        'pr_col': 5,

        # 是否展示看板信息
        'board': False,
    }, {
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 预备营】飞桨启航计划集训营（第三期）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2024-06-19T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/65279',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id' : 5,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Starter Code Camp"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-5']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Starter Code Camp",

        # PR、状态等信息所在的列
        'pr_col': 4,

        'board': False,
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
