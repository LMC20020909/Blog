---
title: ubuntu22.04安装MySQL8.0(无root权限)
date: 2023-03-10 18:19:27
updated: 2023-03-10 18:19:27
categories: [教程, server]
tags: [教程, server,Linux,MySQL]
excerpt: 在没有root权限的服务器(ubuntu22.04)上安装MySQL8.0，主要区别是不能使用sudo命令
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230310_bg1.jpg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230310_bg1.jpg
---

### 下载安装包

官网地址：https://downloads.mysql.com/archives/community/

![image-20230310182201692](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20230310182201692.png)

虽然服务器的系统是ubuntu22.04，但本人在网上所找到的所有教程无论是centos还是ubuntu系统都选择了Linux-Generic的版本进行下载。Generic不是某一操作系统，而是Linux通用的内核，所以一般适用于常见的Linux系统。

查看内核版本命令：

```bash
cat /proc/version
```

如果带有generic字样则可以安装Linux-Generic版本。

注意下面选项中不同的glibc版本

> &emsp;&emsp;glibc是GNU发布的libc库，即c运行库。glibc是linux系统中最底层的api，几乎其它任何运行库都会依赖于glibc。glibc除了封装linux操作系统所提供的系统服务外，它本身也提供了许多其它一些必要功能服务的实现。由于 glibc 囊括了几乎所有的 UNIX 通行的标准，可以想见其内容包罗万象。而就像其他的 UNIX 系统一样，其内含的档案群分散于系统的树状目录结构中，像一个支架一般撑起整个操作系统。在 GNU/Linux 系统中，其C函式库发展史点出了GNU/Linux 演进的几个重要里程碑，用 glibc 作为系统的C函式库，是GNU/Linux演进的一个重要里程碑。

查看系统glibc支持的版本：
~~~bash
strings  /lib/x86_64-linux-gnu/libc.so.6 | grep GLIBC_
~~~

下载对应版本的安装包即可

下载方式：右键download复制下载地址（注意是32位还是64位）

```bash
wget https://downloads.mysql.com/archives/get/p/23/file/mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz
```

### 解压

注意，如果有权限的话，优先把mysql装在/usr/local中，因为这是mysql默认的路径，会省去很多麻烦，但一般用户可能没有权限访问，那么可以安装在用户文件夹下，如/home/username/mysql。

```bash
tar -xvf mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz
```

```bash
mv mysql-8.0.31-linux-glibc2.12-x86_64 mysql8.0		//重命名
```

### 新增修改配置文件

```bash
cd mysql8.0
```

新建配置文件my.cnf，**注意修改对应文件的路径**

```bash
[client]
port=3306
socket=/home/username/mysql/mysql8.0/mysql.sock

[mysqld]
# 服务端口号
port=3306

# mysql安装根目录
basedir=/home/username/mysql/mysql8.0

# mysql数据文件所在位置
datadir=/home/username/mysql/mysql8.0/data

# mysql进程文件
pid-file=/home/username/mysql/mysql8.0/mysql.pid

# 设置socke文件所在目录
socket=/home/username/mysql/mysql8.0/mysql.sock

# 数据库错误日志文件
log_error=/home/username/mysql/mysql8.0/error.log
server-id=100

# 数据库默认字符集,主流字符集支持一些特殊表情符号（特殊表情符占用4个字节）
character-set-server = utf8mb4

# 数据库字符集对应一些排序等规则，注意要和character-set-server对应
collation-server = utf8mb4_general_ci

# 设置client连接mysql时的字符集,防止乱码
init_connect='SET NAMES utf8mb4'

# 是否对sql语句大小写敏感，1表示不敏感
lower_case_table_names = 1
```

为了保险起见，在对应路径下新建对应的文件

```bash
mkdir data
```

```bash
touch mysql.pid mysql.sock mysql.log
```
将support-files文件夹下三个配置文件中的路径修改为自己的对应位置（默认在/usr/local中）
![image-20230310194603582](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20230310194603582.png)

### 安装并启动mysql

安装

```bash
cd bin
./mysqld --defaults-file=/home/username/mysql/mysql8.0/my.cnf --initialize --user=username --basedir=/home/username/mysql/mysql8.0 --datadir=/home/username/mysql/mysql8.0/data
```

启动

```bash
./mysqld_safe --defaults-file=/home/username/mysql/mysql8.0/my.cnf --user=username &
```

```bash
netstat -tln | grep 3306	//查看是否成功监听3306端口
```

### 登录mysql

获取初始密码

```bash
cd ..	//进入error.log所在路径
less error.log | grep root@localhost	//查找root用户的初始登录密码
```

登录，需要指定mysql.sock的位置，默认是/tmp/mysql.sock

```bash
cd bin
./mysql -u root -p -S /home/username/mysql/mysql8.0/mysql.sock
```

当然也可以建立软连接：

```bash
ln -s /home/username/mysql/mysql8.0/mysql.sock /tmp/mysql.sock
,/mysql -u root -p
```

输入之前获取到的初始密码，即可登录成功。

*（当然也有可能出现各种奇怪的错误，比如缺包什么的，那样的话请自行google）*

### 修改密码

```mysql
use mysql
```

```mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';
```

**注意安装的mysql是8.0的还是之前的版本，语法可能不同**



