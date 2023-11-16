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
        'http': "", #os.environ.get('HTTP_PROXY'),
        'https': "", #os.environ.get('HTTPS_PROXY')
    },

    # 是否展示看板信息
    'board': True,

    'comment_to_user_list': []
}

configs = [
    {
        # 任务名称，起标识作用
        'issue_name': "【黑客松】",

        # 黑客松开始时间，只会统计黑客松开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2023-09-13T00:28:48Z',

        # 黑客松 issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/57262',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls',
             'https://api.github.com/repos/PaddlePaddle/community/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleScience/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleOCR/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleClas/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleSeg/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleDetection/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleNLP/pulls',
             'https://api.github.com/repos/PaddlePaddle/Paddle3D/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleMIX/pulls',
             'https://api.github.com/repos/PaddlePaddle/Paddle2ONNX/pulls',
             'https://api.github.com/repos/ArmDeveloperEcosystem/Paddle-examples-for-AVH/pulls',
             'https://api.github.com/repos/openvinotoolkit/openvino/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaddleCustomDevice/pulls',
             'https://api.github.com/repos/PaddlePaddle/PaConvert/pulls',
             'https://api.github.com/repos/PaddlePaddle/docs/pulls',
             'https://api.github.com/repos/InfiniTensor/InfiniTensor/pulls'
            ],

        # 总的任务数量
        'task_num' : 111,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [],

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["热身赛", "框架 API 开发任务", "框架其他开发任务", "科学计算模型复现", "套件开发任务", "合作伙伴任务"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                        [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 110],
                        [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 101, 102, 103, 104, 105],
                        [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
                        [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87],
                        [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 106, 107, 108, 109, 111]],
        
        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Hackathon.*?No",
        
        # PR、状态等信息所在的列
        'pr_col': 4,

        # 如果需要标识完成人，需要写上完成人所在的列
        'complete_col': 5,
    }, {
        # 任务名称，起标识作用
        'issue_name': "【黑客松】PIR Python API 适配升级",

        # `【黑客松】PIR Python API 适配升级` 任务开始时间，只会统计任务开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2023-10-20T00:00:48Z',

        # 黑客松 issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/58067',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 总的任务数量
        'task_num' : 252,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [68,110],   # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["PIR Python API 适配升级"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-252']],
        
        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "PIR API adaptor No.",
        
        # PR、状态等信息所在的列
        'pr_col': 3,
    },{
        # 任务名称，起标识作用
        'issue_name': "[Docathon] 英文文档格式修复（Fix 'System Message'）",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2023-10-24T00:28:48Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/Paddle/issues/58237',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/Paddle/pulls'],

        # 总的任务数量
        'task_num' : 28,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [18,21], # 已经手动分配出去了

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Docathon"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-28']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Fix System Message No.",

        # PR、状态等信息所在的列
        'pr_col': 3,
        
    },{
        # 任务名称，起标识作用
        'issue_name': "[Docathon] 中文文档 copy-from 清理",

        # 开始时间，只会统计开始时间之后的PR(注意时间中的字母T和Z不能缺少)
        'start_time' : '2023-11-08T00:00:00Z',

        # issue页面 url 地址, 注意结尾不要有斜杠
        'issue_url': 'https://api.github.com/repos/PaddlePaddle/docs/issues/6300',
        
        # 监控的仓库列表
        'repo_urls': ['https://api.github.com/repos/PaddlePaddle/docs/pulls'],

        # 总的任务数量
        'task_num' : 19,

        # 忽略不处理的题号，这部分留给人工处理
        'un_handle_tasks' : [], 

        # 已删除的赛题
        'removed_tasks' : [],

        # 赛道名
        'type_names' : ["Docathon"], 

        # 每个赛题所属的赛道，每个赛道是一个数组
        'task_types' : [['1-19']],

        # 该issue相关PR的前缀，用来标识PR是否属于该issue
        'pr_prefix' : "Fix COPY-FROM No.",

        # PR、状态等信息所在的列
        'pr_col': 3,
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
