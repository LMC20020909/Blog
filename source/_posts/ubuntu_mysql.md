---
title: ubuntu22.04安装MySQL8.0并远程连接(有root权限)
date: 2023-03-08 19:40:39
updated: 2023-03-08 19:40:39
categories: [教程, server]
tags: [教程, server,Linux,MySQL]
excerpt: 在腾讯云服务器(ubuntu22.04)上安装MySQL8.0，在本地用navicat远程连接
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230308_bg1.jpg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230308_bg1.jpg
---
### 安装MySQL

```bash
sudo apt update
```

```bash
sudo apt install mysql-server
```
此时mysql服务应该已经自动开启

```bash
systemctl status mysql	//查看mysql运行状态
```
### 设置用户并更改密码

此时mysql默认创建了一个root用户，密码为空，可以直接登录

```bash
sudo mysql -u root	//注意一定要sudo！
```
更改root用户的密码
```bash
alter user 'root'@'localhost' identified with mysql_native_password by 'your_new _password';
```
设置mysql安全配置
```bash
sudo mysql_secure_installation
```

注意这里会让你输入密码的安全等级，如果你之前设置（或者没设置）的root用户密码不符合你输入的等级会让你更改密码
如果对密码安全性没有要求的话可以全部填n

### 配置远程连接

初始情况下有4个数据库，mysql数据库中user表的host属性代表该用户可以连接的ip地址

将root用户的host修改为‘%’，即表示任何ip都可连接

```bash
update mysql.user set host='%' where user='root';
```

![image-20230308200034784](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20230308200034784.png)
```bash
grant all on *.* to 'root'@'%';	//授予root用户所有权限
```

```bash
flush privileges;	//刷新
```
#### 修改配置文件

```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

> bind-address = 0.0.0.0
>
> port = 3306	//修改为你想为mysql配置的端口

![image-20230308200318810](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20230308200318810.png)

**一定要重启mysql才能生效**！

```
systemctl restart mysql
```

或者

```bash
service mysql stop;
service mysql start;
```
### 开放端口

首先在腾讯云中的安全组或者防火墙（轻量级服务器）中将3306端口开放，如果此时仍不能连接请往下看

如果放开之后仍无法连接，则可能是服务器内部的防火墙对端口进行了限制，方法如下：

```bash
sudo apt install firewalld		//安装防火墙控制
```
注意，可能会出乱子导致xshell连接不上，原因是安装了firewalld后可能会把所有端口都进行限制，此时登录腾讯云=>vnc登录，然后输入：

```bash
sudo ufw disable
```

回到xshell，输入：

```bash
sudo ufw enable
sudo ufw allow 3306
```

此时就配置完毕了

### navicat远程连接MySQL

![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hc2sucWNsb3VkaW1nLmNvbS9odHRwLXNhdmUveWVoZS0xNzQ5NTM3L3U4ejRmaXM5dDEucG5n?x-oss-process=image/format,png)

