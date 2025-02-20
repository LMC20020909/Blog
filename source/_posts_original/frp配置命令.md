---
title: frp配置命令
date: 2023-08-07 13:45:04
updated: 2023-08-07 13:45:04
categories: [教程, server]
tags: [教程, server,frp,jupyter]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230807_bg1.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230807_bg1.jpg
---

通过具有公网ip的跳板机访问内网服务器
<!--more-->

### 服务端（公网服务器）

启动frps

```bash
nohup ./frps -c frps.ini > ./frps.out 2>&1 &
```

关闭frps

```bash
ps -aux | grep 'frps'
kill -9 xxx
```

### 客户端

启动frpc

```bash
nohup ./frpc -c frpc.ini > ./frpc.out 2>&1 &
```

关闭frpc

```bash
ps -aux | grep 'frpc'
kill -9 xxx
```

启动jupyter notebook

```bash
nohup jupyter notebook > /home/mindle-env/.jupyter/log.out 2>&1 &
```

关闭jupyter notebook

```bash
ps -aux | grep 'jupyter-notebook'
kill -9 xxx
```



