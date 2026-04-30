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
        'issue_name': "【Hackathon 10th】PaddleOCR+ERNIE 应用创新赛道",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2026-03-18T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/78325',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id': 1,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["PaddleOCR+ERNIE 应用创新赛道"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types': [['1']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix': "Hackathon 10th OCR+ERNIE No.",

        # PR、状态等信息所在的列（0-indexed，报名情况列）
        'pr_col': 4,

        # 是否展示看板信息
        'board': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 10th ERNIE with Partners】文心合作伙伴赛道",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2026-03-25T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/78485',

        # 监控的仓库列表
        'repo_urls': [],

        # 最大的任务ID
        'max_task_id': 29,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["打卡任务", "进阶任务", "开源贡献任务"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types': [['1-12'], ['13-28'], ['29']],

        # PR、状态等信息所在的列（报名名单列）
        'pr_col': 5,

        # 是否展示看板信息
        'board': False,
    },{
        # 任务名称，起标识作用
        'issue_name': "【HACKATHON 10th】PaddleOCR 全球衍生模型挑战赛",

        # issue页面 url 地址，注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/PaddleOCR/issues/17858',

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time': '2026-03-25T00:00:00Z',

        # 监控的仓库列表（竞赛制，不追踪 PR）
        'repo_urls': [],

        # 最大的任务ID（仅1个报名任务）
        'max_task_id': 1,

        # 忽略不处理的题号
        'un_handle_tasks': [],

        # 已删除的赛题
        'removed_tasks': [],

        # 赛道名
        'type_names': ["报名"],

        # 每个赛题所属的赛道
        'task_types': [['1']],

        # PR、状态等信息所在的列（报名追踪列）
        'pr_col': 4,

        # 是否展示看板信息
        'board': False,
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
                      'https://api.github.com/repos/PFCCLab/paddle_sparse/pulls',
                      'https://api.github.com/repos/PFCCLab/paddle_geometric/pulls',
                      'https://api.github.com/repos/PaddlePaddle/community/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleScience/pulls',
                      'https://api.github.com/repos/PaddlePaddle/PaddleMaterials/pulls'],

        # 最大的任务ID
        'max_task_id' : 53,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["框架开发任务", "科学计算任务", "FastDeploy套件开发任务"],

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-2','51-52'], ['3-19'], ['20-50','53']],

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
