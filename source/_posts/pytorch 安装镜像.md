---
title: Pytorch 安装镜像
date: 2024-12-15
updated: 2024-12-15
excerpt: Pytorch 安装指定版本，然官方下载链接太慢
categories: [教程,server]
tags: [教程,server,pytorch,python,pip]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241215_bg2.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241215_bg2.jpg
---

我们都知道安装 pytorch 需要根据机器的 cuda 版本相对应，我们也知道在国内使用 pip 安装的时候最好进行换源以加快下载速度。正常的安装方式应该是：

```bash
pip3 install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple
```

但当 cuda 版本并不匹配时，就需要另请高明。

> pytorch 与 cuda 版本并不一一对应，也不总是向下兼容。例如，对于 cuda 12.2，安装对应 cuda 12.4 的 pytorch 版本就会出现问题，而安装 cuda 12.1 的 pytorch 版本就没问题。***因此，在选择版本时最好选择比自己 cuda 版本低的里面最高的一个对应的 pytorch 版本。***

例如我们想要安装 cuda 12.1 对应的 pytorch，按照官网的指令 https://pytorch.org/get-started/locally/：

```bsah
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

但此时 -i 参数与我们想要换源的镜像地址冲突，直接运行这个命令下载速度可能会非常感人，因此我们需要找到一个镜像网站。



截止到 2024.12.15，目前可用的方法如下：

1. 在阿里云的镜像网站：https://mirrors.aliyun.com/pytorch-wheels/ 中找到想安装的 torch 对应的 cuda 版本的目录。例如对于 cuda 12.1，进入 https://mirrors.aliyun.com/pytorch-wheels/cu121/；

2. 在其中找到对应的 torch, torchvision, torchaudio 版本（与 python 版本、系统架构有关），下载 whl 安装包；

3. 手动安装

   ```bash
   pip install filename.whl
   ```



**参考文章**

1. [阿里云镜像源加速下载Pytorch whl](https://hiyyq.cn/posts/20240217165828/)
