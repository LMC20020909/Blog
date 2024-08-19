---
title: 记录一下git出现的奇怪错误 
date: 2022-11-14 16:26:51
updated: 2022-11-14 16:26:51
categories: bug
tags: [bug, git, github]
excerpt: 突然git push不上去了...
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg6.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg6.jpg
---

&emsp;&emsp;今天git push的时候突然给我报了一些诡异的错误，按照以往的经验，git不上去通常是网络问题。然而当时校园网已经断了，而不知道为什么我用手机热点无法访问github，提示我不是私密链接，输入了“thisisunsafe”也不行，只有科学上网才行。于是我用@hust的方式续了续校园网，发现github能访问了，但还是git不上去。 而且在我一顿操作后，居然要我输入用户名和密码。我赶紧重新配置了一下：

```bash
git config --global user.name "xxx"
git config --global user.email "xxx"
```

git push的时候还是让我输用户名和密码，并且输了之后还是报错：

```bash
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/xxx.git/'
```

上网一查，发现github自从 2021 年 8 月 13 日后不再支持用户名密码的方式验证了，需要创建个人访问令牌(personal access token)。按照[网上的教程](https://blog.csdn.net/qq_50840738/article/details/125087816)设置了一番，再次git push，还是不行。

报错信息：

```bash
fatal: unable to access 'https://github.com/xxx.git/': OpenSSL SSL_read: Connection was reset, errno 10054
```

看样子是ssl验证的问题。按照网上的说法设置：

```bash
git config --global http.sslVerify "false"
```

再次git push，换了一个错误：

```bash
fatal: unable to access 'https://github.com/xxx.git/': Failed to connect to github.com port 443: Timed out
```

网上查了一下说是代理的问题，可是此时我是正常上网，而且github可以正常访问。看来网上的教程不能轻信。我决定先ping一下github看看：

```bash
ping github.com
```

果然：

```bash
Pinging github.com [20.205.243.166] with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 20.205.243.166:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
```

我又ping了一下百度，完全没问题，看来可能是我之前的一顿操作把电脑里默认的github的ip地址给改了。于是按照[网上教程](https://blog.csdn.net/sang_12345/article/details/126869608)一顿操作（host文件无法修改的话右键->属性->安全把权限改一下就行了）。发现果然可以ping通了。再次git push成功。虽然问题是解决了，但这github的访问实在是玄学。但本人现在对计网是一窍不通，看来有空得琢磨琢磨是怎么回事了。



为了能在不同的网络类型和上网方式的排列组合下都能git push，我反复试了多次，发现科学上网会影响git的代理。

取消代理：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```



### 总结

总体来看就两种错误：

#### errno 10054

```bash
fatal: unable to access 'https://github.com/xxx.git/': OpenSSL SSL_read: Connection was reset, errno 10054
```

解决方法：

```bash
git config --global http.sslVerify "false"
```

#### errno 443: Timed out

最恶心、最玄学的错误

```bash
ping github.com
```

##### 不能ping通

照着[网上教程](https://blog.csdn.net/sang_12345/article/details/126869608)设置一下ip。

##### 能ping通

+ 根据[教程](https://blog.csdn.net/qq_29545715/article/details/103576549?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-103576549-blog-46842191.pc_relevant_3mothn_strategy_and_data_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-103576549-blog-46842191.pc_relevant_3mothn_strategy_and_data_recovery&utm_relevant_index=4)设置取消代理。此法有时管用，有时无效。
+ 关掉vpn再试试。
+ 还不行的话，反复开关vpn试试。
+ 多push几次。





