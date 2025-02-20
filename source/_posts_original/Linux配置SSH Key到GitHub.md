---
title: Linux配置SSH Key到GitHub 
date: 2023-01-07 21:50:57
updated: 2023-01-07 21:50:57
categories: [教程, server]
tags: [教程, server, linux, git, github]
excerpt: 总体上和windows差不多，但出了点小问题。
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg12.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg12.jpg
---

## Git本地环境配置

### 安装git

```bash
sudo apt-get install git
```

### 配置用户信息

```bash
git config --global user.name "Your Name"
git config --global user.email Your_email@example.com
```

### 查看配置信息

```bash
git config --list
```



## 配置SSH连接Github

### 安装SSH

```bash
sudo apt-get install ssh
```

### 创建密钥文件

```bash
ssh-keygen -t rsa -C "你的github账号邮箱"
```

首先 ssh-keygen 会确认密钥的存储位置和文件名（默认是 .ssh/id_rsa）,然后他会要求你输入两次密钥口令，留空即可。所以一般选用默认，全部回车即可。

默认密钥文件路径在`~/.ssh`，`id_rsa`是私钥文件，`id_rsa.pub`是公钥文件

### 将公钥添加到Github

1. 将`id_rsa.pub`文件内容全部复制

2. 登陆到GitHub上，右上角小头像->Setting->SSH and GPG keys中，点击new SSH key。

### SSH测试

在终端输入：

```bash
ssh -T git@github.com
```

如果结果为 “ ...You've successfully authenticated, but GitHub does not provide shell access”，则说明成功。



## Bug

### SSH测试结果为要求输入密码

如果上一步结果为“git@github.com's password:”则需要修改配置文件。

详见官方文档：https://docs.github.com/cn/authentication/troubleshooting-ssh/using-ssh-over-the-https-port

配置文件位置在/etc/ssh/ssh_config

### 解决上传ssh-key后git push仍须输入密码的问题

如果我们使用https方式克隆的仓库：

```bash
git clone https://github.com/Name/project.git
```

这样便会在你git push时候要求输入用户名和密码。
解决的方法是使用ssh方式克隆仓库：

```bash
git clone git@github.com:Name/project.git
```

当如，如果已经用https方式克隆了仓库，就不必删除仓库重新克隆，只需将 .git/config文件中的

```bash
url = https://github.com/Name/project.git
```

一行改为

```bash
url = git@github.com:Name/project.git
```


即可。



## References

1. https://segmentfault.com/a/1190000013154540
2. https://blog.csdn.net/yuzhiqiang_1993/article/details/127032178
3. https://blog.csdn.net/baidu_35085676/article/details/53456884
