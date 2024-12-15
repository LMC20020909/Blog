---
title: Tmux 常用操作
date: 2024-12-15
updated: 2024-12-15
excerpt: Tmux 常用操作命令汇总
categories: [教程,server]
tags: [教程,server,tmux]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241213_bg1.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241213_bg1.jpg
---

# Intro

Tmux，全称为 terminal multiplexer，其功能不必多言。

tmux 分为三个层次：***session*** (会话), ***window*** (窗口), ***pane*** (面板)。其没有严格的使用区分，只涉及到生命周期和从属关系，可以根据需求和使用习惯进行分配使用。



# 常用命令和快捷键

### session 操作

**new 操作：新建 session**

1. 不需要指定名字，随便新建一个：

   ```bash
   tmux
   ```

  或者：

   ```bash
   tmux new
   ```

2. 新建并取名

   ```bash
   tmux new -s name
   ```

**detatch 操作：从 session 中脱离返回 terminal**

```bash
Ctrl B + D
```

**attach 操作：从 terminal 进入 detatched session**

1. 查看当前所有 session

   ```bash
   tmux ls
   ```

2. 指定 session 名字进入

   ```bash
   tmux a -t name
   ```

   *如果直接 `tmux a` 会默认 attach 最近的 session*

**kill 操作：永久 kill session**

1. 在 session 内部 kill 当前 session

   ```bash
   Ctrl D
   ```

2. 在 terminal kill 指定 session

   ```bash
   tmux kill-session -t name
   ```

   *同理，如果直接 `tmux kill-session` 会默认 kill 最近的 session*

3. 在 terminal kill 所有存在的 session

   ```bash
   tmux kill-server
   ```

**rename 操作：重命名 session**

1. 在 session 内部 rename current session

   ```bash
   Ctrl B + $
   ```

   然后输入新的名字

2. 在 terminal rename certain session

   ```bash
   tmux rename-session -t old_name new_name
   ```

   *同理，如果不指定 -t 直接 `tmux rename-session new_name` 会默认 rename 最近的 session*



### window 操作

window 是从属于某个 session 的界面，创建 session 时会默认创建一个 window

**new 操作：新建 window**

在 session 内部，

```bash
Ctrl B + C
```

**不同 window 之间切换**

1. 下一个

   ```bash
   Ctrl B + N
   ```

2. 上一个

   ```bash
   Ctrl B + P
   ```

3. 根据 window 的序号进行切换

   ```bash
   Ctrl B + 0/1/2/...
   ```

4. 显示全局所有 window 信息并通过方向键+回车切换：

   ```bash
   Ctrl B + W
   ```

**rename 操作：重命名 window**

```bash
Ctrl B + ,
```

**kill 操作：kill window**

```bash
Ctrl B + &
```



### Pane 操作

pane 是从属于 window 的面板，一个 window 可以切分成多个 pane

**new 操作：新建 pane**

1. 左右切分面板

   ```bash
   Ctrl B + %
   ```

2. 上下切分面板

   ```bash
   Ctrl B + ""
   ```

**pane 之间切换**

1. 方向键切换

   ```bash
   Ctrl B + 方向键
   ```

2. 根据序号切换

   查看序号索引：

   ```bash
   Ctrl B + Q
   ```

   根据序号进行切换：

   ```bash
   Ctrl B + Q + 0/1/2/...
   ```

**kill 操作：kill pane**

```bash
Ctrl B + X
```



# Configuration

### 在 tmux 中启用鼠标

在默认的 tmux 中，鼠标使用受到了很大的限制，包括滚轮、滑动选中都无法正常使用，因此需要在配置文件中启用鼠标控制。

1. 打开（新建）配置文件：

   ```bash
   vi ~/.tmux.conf
   ```

2. 启用鼠标，写入配置文件：

   ```bash
   set -g mouse on
   setw -g mode-keys vi
   ```

   第一条配置是启用鼠标，第二条是启用 vim 模式，可以方便进行复制粘贴。此时用鼠标滚轮选中 tmux 中的任何输出就会默认复制到剪贴板。
