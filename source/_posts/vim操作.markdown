---
title: vim 常用操作
date: 2026-01-08 22:31:00
updated: 2026-01-08 22:31:00
categories: [教程, server]
tags: [教程, server, vim]
excerpt: 在 vscode 上安装了 vim 插件，尝试熟悉使用，尽量脱离鼠标操作
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20260315_bg3.jpg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20260315_bg3.jpg
---

o: 在下面建立空行进入插入模式

O: 在上面建立空行进入插入模式

shift i: 光标跳到行首进入插入模式

shift a: 光标跳到行尾进入插入模式

hjkl: 左下上右

0: 跳到当前行绝对开头

$: 跳到当前行末尾

^: 跳到当前行开头

w: 跳到下一个单词开头

b: 跳到上一个单词开头

gg: 跳到文件开头

G: 跳到文件末尾

{: 跳到上一个空行

}: 跳到下一个空行

行号+gg, 行号+G, :行号+enter: 跳转到指定行

dd: 剪切当前行

3dd: 剪切当前行和下面两行

yy: 复制当前行

3yy: 复制当前行和下面两行

gc{motion}: 注释

- gcc: 注释当前行
- gc3j: 注释当前行和向下两行

u: undo change

