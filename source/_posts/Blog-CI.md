---
title: Blog CI
date: 2024-08-19 17:47:30
updated: 2024-08-19 17:47:30
excerpt: 利用 github action 实现博客自动化部署并多端同步
categories: 博客
tags: [博客,github,教程]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20240819_bg5.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20240819_bg5.jpg
---

最近新配了一台主机，加上 macbook 和老笔记本一共就有了三台设备。俗话说得好，有新的不用旧的，这个博客的环境和数据都保存在老笔记本上，每次想发点什么东西还要特意打开它，十分麻烦。加上三台电脑一般被我放在三个地方，于是就有了随时随地写、随时随地发的需求。本来想的是将博客移植到新主机上面去，但在搜索攻略的时候发现有一种能够免配环境、自动部署、多端同步的处理方式正合我意，毕竟处于需求隔离的想法，暂时还不是很想对另外两台设备动过多的手脚。

通俗来讲，这种方式之所以有效，本质上是相当于把原来在电脑本地配置安装的 hexo 博客环境和数据转移到 github 的服务器上，这样就不用在本地安装 NodeJS 和 hexo 环境。同时编写一个自动化脚本，利用 github actions 功能，每当博客的源代码有更新时自动编译，并将静态文件推送到 github.io 的仓库中。

### 建仓

为了实现这一需求，我们需要准备两个 github repo，一个用来存放博客的源代码，一个用来存放网页的静态文件。如果你在本地已经使用过博客，那么后一个仓库，也就是你的 username.github.io 仓库，应该已经准备好了，在此不再赘述；前一个 repo 我起名为 Blog，设置为 private（毕竟是存放源码的地方，需要考虑隐私性）。建好之后，就可以将你在本地的博客源代码一个不剩的全部 push 上去了。注意是把整个根目录都推送上去，包括博客的配置文件等。具体操作如下：

```bash
# 我的本地博客的根目录为 Blog
cd Blog/
git init
git remote add origin xxx
git branch -M main
git add .
git commit -m "xxx"
git push -f origin main
```

在此过程中，可能会出现 git add . 时出错的情况。这是因为在目录下存在着其他 git 仓库，而 git 并不支持嵌套仓库。排查发现是 themes/next 目录是一个 git 仓库。最简单直接的方法就是把 themes/next 目录下的 **.git 文件夹删掉**，这样我们的主题文件夹就是一个普通的目录，而不是一个 git 仓库，这样嵌套仓库的内容就会成为当前仓库内容的一部分，就可以使用 git add 对这些文件进行跟踪。这样做的代价就是无法自动更新主题，但实际上主题的更新与博客的内容无关，且周期很长，所以无伤大雅。删掉之后重新 add commit push 就可以了。

### 赋予权限

在此之后，我们需要赋予这个 Blog 仓库向另一个仓库（github.io）推送代码的权限。你可以把这个存放着博客源代码的仓库当作一个云端服务器，每次向它 push 代码就相当于在这个 server 上编译博客并向 github.io 推送，所以就像我们在本地使用 git 一样，需要有权限访问更改你的 repo。

在 Github 中这种权限验证方式有三种：

1. 用户名密码，最古早的方式，在2021年就基本已被弃用；
2. SSH 密钥验证，目前最主要的方式，只要公钥存放在你的 Github 账户里，拥有对应私钥的一方就拥有了访问更改你仓库的权限；
3. Token 链接，与 SSH 的相比，好处是你可以对每个 token 的权限进行更加细化的设置，如访问、更改、删除等，坏处是 token 的验证是单向的，而我们一般为了图方便都会给 token 赋予最高权限，换句话说，拥有了你的 token 的一方相当于掌握了你的密码，安全性难以保证。

当然，为了赋予 Blog 仓库权限，我们无论是使用 SSH 还是 Token，都需要把一个有权限的 SSH 私钥或是 token 上传到云端，似乎安全性都无法保证。但实际上，GitHub 提供了在仓库中设置机密（Secrets）的功能，允许将敏感信息（如 token 或 密钥）安全地存储并在工作流中使用。GitHub 通过加密和访问控制来保护这些机密，避免在构建过程中泄露。使用 SSH 验证只需要上传私钥就行，而使用 Token 还需要对博客的配置文件中的 deploy 地址进行更改。基于最小化实现原则，本人选择了 SSH 的方式。具体操作如下：

1. 找一个已有的有效密钥，即公钥已经添加到了你的 Github 设置中。如果没有或者不想重用的话，可以再新生成一个然后将公钥添加好：
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```

2. 将私钥添加到 Blog 仓库中：
   ![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191908522.png)

	这里我取名为 HEXO_DEPLOY_PRIVATE_KEY_DELL_RSA。注意，在复制私钥的时候一定要全体复制，直接 ctrl A + ctrl C，否则可能会因格式不对而无法验证权限。

### 添加 GitHub Actions 脚本

你可以把 GitHub Actions 功能当作触发器，当你设定的某个条件满足时出发相应的动作。我们的需求是当博客更新 push 时，自动编译并部署。所以在这里触发器的条件就是主分支有新的 push，触发的动作就是配置 hexo 博客环境并编译部署，也就是之前我们在本地做的那一套。

点击 Blog 仓库的 `Actions`。

![image-20240819192224011](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191922048.png)

点击 `New workflow`。

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191923074.png)

点击 `set up a new workflow yourself`。

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191924277.png)
