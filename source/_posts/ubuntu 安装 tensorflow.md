---
title: ubuntu 安装 tensorflow
updated: 2023-12-23 11:58:01
categories: [教程, server]
tags: [教程, server, tensorflow, linux]
excerpt: 轻松安装gpu版本
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20231223_bg2.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20231223_bg2.jpg
---

# ubuntu 安装 tensorflow

1. 查看系统CUDA版本

   ![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202312202306943.png)

   

2. 上官网查看CUDA版本对应的tensorflow版本以及python版本：https://www.tensorflow.org/install/source#gpu

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202312202308089.png)

需要安装2.15.0版本的tensorflow，并且python版本要在3.9-3.11之间（划重点），python版本对应不上会安装不了对应版本的tensorflow

3. 安装tensoorflow：https://www.tensorflow.org/install/pip（注意要看英文版的官网，和中文版的还不一样）

   ```python
   # For GPU users
   pip install tensorflow[and-cuda]
   # For CPU users
   pip install tensorflow
   ```

4. 验证是否安装成功，gpu是否可用

   ```python
   import tensorflow as tf
   print(tf.config.list_physical_devices('GPU'))
   ```

   

