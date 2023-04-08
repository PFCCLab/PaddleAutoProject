# WeChatBot

见 https://github.com/PaddlePaddle/Paddle/discussions/51802#discussioncomment-5485356

## 设计目标

构建一个能够监听微信指定群聊，并根据群聊信息返回指定字段的机器人。

## 初步目标

1. 构建一个机器人，能够根据指定关键词触发回复“Hello!”
2. 当收到关键词后，能够检索指定github上的快乐开源表单，反馈表单信息

## 当前进展

设计思路为，通过PyQt构建前端页面，定期截取当前微信聊天页面，并通过OCR检查关键词，回复对应内容。

## 鸣谢
- https://blog.csdn.net/kaida1234/article/details/86497461 感谢关于Qt5的屏幕截图的示例代码
- https://zhuanlan.zhihu.com/p/385978085 图片判断
- https://blog.csdn.net/qq_46026178/article/details/120924385 鼠标移动和键盘输入