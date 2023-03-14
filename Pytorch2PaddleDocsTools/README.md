# PyTorch与Paddle文档映射辅助工具

具体起源与需求见 https://github.com/PaddlePaddle/docs/issues/5691

## Call for Contributor
- utils 缺少对html页面的解析函数，需要将html页面解析为字典
- main::getweb 缺少将字典信息填充到组件的逻辑
- main::write_md 缺少根据组件信息构造md文档的逻辑
- 其他，如在API名称下增加选项按钮，用于人工指定当前对比的API属于“Torch此参数多”、“Paddle参数多”、“完全一致”等情况。