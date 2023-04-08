# WeChatBot

见 https://github.com/PaddlePaddle/Paddle/discussions/51802#discussioncomment-5485356

## 设计目标

构建一个能够监听微信指定群聊，并根据群聊信息返回指定字段的机器人。

## 初步目标

1. 构建一个机器人，能够根据指定关键词触发回复“Hello!”
2. 当收到关键词后，能够检索指定github上的快乐开源表单，反馈表单信息

## 当前进展

设计思路为，通过PyQt构建前端页面，定期截取当前微信聊天页面，并通过OCR检查关键词，回复对应内容。