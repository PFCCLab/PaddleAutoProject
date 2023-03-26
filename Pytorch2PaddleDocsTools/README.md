# PyTorch与Paddle文档映射辅助工具

具体起源与需求见 https://github.com/PaddlePaddle/docs/issues/5691

## Call for Contributor

https://github.com/PFCCLab/PaddleAutoProject/issues/13

## 已知问题

打包后的 macos app 打不开的话需要手动给权限才能运行 `chmod +x Pytorch2PaddleDocsTools.app/Contents/MacOS/Pytorch2PaddleDocsTools`

## 如何使用？

### 一、配置环境

1. 首先将PaddleAutoProject克隆到本地

~~~shell
# 在Git bash内
git clone https://github.com/PFCCLab/PaddleAutoProject.git
~~~

2. 打开自己的IDE，并进入到Pytorch2PaddleDocsTools文件夹下

~~~shell
cd .\xxx\PaddleAutoProject\Pytorch2PaddleDocsTools
~~~

3. 下载所需依赖

~~~shell
pip install -r requirements.txt
~~~

4. 一键启动项目~

~~~shell
python .\main.py
~~~

### 二、如何从 0 开始完成一个文档任务

如果我们正常打开项目，可以看到以下界面，下面将以此介绍其功能。

<img src="README/image-20230326143836410.png" alt="image-20230326143836410" style="zoom:50%;" />



- Save Directory：最终写出文件的保存路径，默认为当前目录下
- PyTorch API url：所需修复文档的PyTorch API 链接
- PaddlePaddle API url：所需修复文档的PaddlePaddld API 链接

#### 1.查找所需 API 的url

当我们点击工具中的`打开api文档网站`按钮，可以进入Paddle与Pytorch的官方文档，此时可以搜索我们所需要修改的API，例如案例中的`abs`。

![image-20230326150019973](README/image-20230326150019973.png)

![image-20230326145955177](README/image-20230326145955177.png)

当按照图上顺序点击后，此时网页上方出现的URL即为我们所需填写的URL，可以将其填写在`PyTorch API url`与`PaddlePaddle API url`框内。

![image-20230326150244192](README/image-20230326150244192.png)

![image-20230326150220704](README/image-20230326150220704.png)

![image-20230326150421573](README/image-20230326150421573.png)

#### 2.解析网页并判断文档映射类型

由于abs文档属于无参数映射关系，故可以先选择其类型，并且点击解析网页。

![image-20230326150807843](README/image-20230326150807843.png)

后得到解析成功后的结果：

![image-20230326150955783](README/image-20230326150955783.png)

若解析有误，可以自行点击上方图中`增加一行`/`减少一行`进行调整，当出现参数有差异的情况，并可补充备注。

对于需要进行转写的案例，本工具也可自动生成转写案例（如下图），由于`abs`为无参数案例，故自动忽略其转写实例，并且也无需补充备注，故可以直接点击写文件进行文本导出，导出路径即为`Save Directory`所配置路径。

![image-20230326152559277](README/image-20230326152559277.png)

现在我们就可以将已经生成好的文档用来提交PR啦~~

![image-20230326152759497](README/image-20230326152759497.png)