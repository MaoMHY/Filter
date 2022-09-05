# 项目介绍：

该方案是基于文心大模型中的情感分析api设计的智能弹幕过滤器。启用弹幕过滤器后，用户看到的所有弹幕都是正向的。

我们的demo是一个有前后端响应的网页。前端部分是对github中的某个开源项目（ https://github.com/Caronell/blingbling ）进行二次开发，后端由flask框架搭建而成。


# 环境搭建：

```
!pip install wenxin_api
!pip install flask
```

运行
=======
因为视频文件太大不方便上传github，所以使用前需要自行在static/video/目录下添加一个名为abcd.mp4的视频文件。
运行main.py后根据提示打开浏览器访问127.0.0.1:5000即可。
