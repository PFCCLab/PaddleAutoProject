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
        'issue_name': "【Hackathon 10th】Fundable Projects",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2026-02-03T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/77444',

        # 监控的仓库列表
        'repo_urls':  [],

        # 最大的任务ID
        'max_task_id' : 2,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Fundable Projects"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-2']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 10th Fundable Projects No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "【Hackathon 10th】开源贡献个人挑战赛 · 春节特别季",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2026-01-19T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/77429',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls',
                      'https://api.github.com/repos/PaddlePaddle/docs/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaConvert/pulls',
                      'https://api.github.com/repos/PaddlePaddle/FastDeploy/pulls',
                      'https://api.github.com/repos/PFCCLab/PaddleAPITest/pulls',
                      'https://api.github.com/repos/PaddlePaddle/community/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleScience/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleMaterials/pulls'],

        # 最大的任务ID
        'max_task_id' : 50,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["框架开发任务", "科学计算任务", "FastDeploy套件开发任务"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-2'], ['3-19'], ['20-50']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 10th Spring No.",

        # PR、状态等信息所在的列
        'pr_col': 4,

        # 是否展示看板信息
        'board': True,
        
        # 如果需要标识完成人，需要写上完成人所在的列
        'complete_col': 5,

        # 是否为黑客松任务
        'hackathon': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "[实习招募] 飞桨正式实习生招募（长期 / 高强度 / 高含金量项目）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2026-01-04T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/77190',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id' : 11,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [''],

        # 赛道名
        'type_names' : ["飞桨正式实习生招募"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "paddle-official-internship",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': False,

        # 是否为黑客松任务
        'hackathon': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 10th Code Camp】护航计划集训营（提前批）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-12-19T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/76977',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id' : 7,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [''],

        # 赛道名
        'type_names' : ["护航计划集训营（提前批）"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-6']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon 10th No.",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': False,

        # 是否为黑客松任务
        'hackathon': True,
    },{
        # 任务名称，起标识作用
        'issue_name': "PaddleMaterials 数据集适配",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-09-12T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleMaterials/issues/191',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/PaddleMaterials/pulls'],

        # 最大的任务ID
        'max_task_id' : 14,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["PaddleMaterials 数据集适配"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-14']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PPMat Dataset No",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': True,

        # 是否为黑客松任务
        'hackathon': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "PaddlePaddle API兼容性增强",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2025-11-10T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/76301',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls',
                      'https://api.github.com/repos/PaddlePaddle/docs/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaConvert/pulls'],

        # 最大的任务ID
        'max_task_id' : 346,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["PaddlePaddle API兼容性增强"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-346']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "API Compatibility No",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': True,

        # 是否为黑客松任务
        'hackathon': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 预备营】飞桨启航计划集训营（马年新春版）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2026-01-26T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/77510',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id' : 1,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["飞桨启航计划集训营（马年新春版）"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "",

        # PR、状态等信息所在的列
        'pr_col': 3,

        # 是否展示看板信息
        'board': False,

        # 是否为黑客松任务
        'hackathon': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "【快乐开源】PaddlePaddle 文档链接修复任务",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2026-01-26T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/docs/issues/7735',

        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/docs/pulls',
                      'https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 最大的任务ID
        'max_task_id' : 126,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["赛道一", "赛道二"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-74'],['75-126']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Doc Link Fix No",

        # PR、状态等信息所在的列
        'pr_col': 5,

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
