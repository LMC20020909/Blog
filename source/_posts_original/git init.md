---
title: Git 基本操作
date: 2022-11-23 10:27:25
updated: 2022-11-23 10:27:25
categories: [教程, git]
tags: [教程, git, github]
excerpt: 防止自己总忘，干脆总结一下
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg7.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg7.jpg
---

## 将远程仓库克隆到本地

```bash
git clone git@github.com:xxx.git
```

```bash
git add .
```

```bash
git commit -m "xxx"
```

```bash
git push
```

## 将本地仓库连接到远程仓库

```bash
git init
```
切换到main分支（git默认分支是master但github默认主分支是main，不改的话上传时会自动创建一个master分支）

```bash
git checkout -b main
```

```bash
git remote add origin git@github.com:xxx.git
```

```bash
git add .
```

```bash
git commit -m "xxx"
```

强制push到main分支，会取代远程仓库中已有的文件
```bash
git push -u origin main -f
```

之后再上传时：

```bash
git push
```

## 同步远程仓库的文件到本地

```bash
git pull origin main
```

## 将本地仓库恢复为之前状态

```bash
git reset --soft HEAD~1	// 回退到上一个版本
```

```bash
git log // 查看commit记录，此时最新的提交记录应变为了上一次的commit
```

https://m.runoob.com/git/git-reset.html
