---
title: Linux 有用且有趣的命令汇总
date: 2024-12-15
updated: 2024-12-15
excerpt: Linux 有用且有趣的命令汇总，如检测 gpu 状态、查看空间大小等
categories: [教程,server]
tags: [教程,server,linux]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241215_bg3.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241215_bg3.jpg
---

#### watch 命令

`watch` 是一个周期性执行程序，并将结果显示到终端上。该命令可以帮助用户监控任何命令的输出变化，这对于需要持续检测系统状态或者文件内容变化的情况非常有用。

##### 基础命令格式

```bash
watch [选项] 命令
```

这里的 `命令 `是指任何可以在shell中执行的命令或者脚本，而 `选项` 则可以用来定制 `watch` 命令的行为。

##### 核心选项与参数

**更新频率**

默认情况下，`watch` 每2秒刷新一次。但可以通过 `-n`  或 `--interval` 选项更改这个频率：

```bash
watch -n 1 ls -l
```

以上命令每1秒更新一次 `ls -l` 的输出。

##### 用法示例

**查看显卡运行状态**

```bash
watch -n 1 gpustat --cpu
```

P.S. 当然，查看显卡运行状态有更好用的工具：

```bash
pip install nvitop
```

```bash
nvitop -m full
```



#### du 命令

`du` 命令用于显示目录或文件所占用的磁盘空间。全称为 `disk usage`。

**查看指定目录的整体大小**

```bash
du -sh name/
```

`du -sh` 查看当前所在目录的大小

**查看当前目录下的子目录和文件的大小**

```bash
du -d 1 -h
```

-d 参数代表深度，1 就是只查看1层的子目录和文件，而不显示子目录中的信息。

`du -d 0 -h` 和 `du -sh` 等价
