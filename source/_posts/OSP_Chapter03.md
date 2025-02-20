---
title: 操作系统原理复习 第三章 用户界面
date: 2022-11-14 16:26:51
updated: 2022-11-14 16:26:51
subtitle: 第三章 用户界面
excerpt: 2020级操作系统原理 苏曙光老师 2022.5.19 第三章 用户界面
categories: [课业, 操作系统原理]
tags: [课业, 操作系统原理,复习,笔记]
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221003_bg3.jpg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221003_bg3.jpg
---

# 用户界面

OS提供给用户控制计算机的机制，又称**用户接口**

类型：

+ **操作界面**
+ **系统调用**

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221003_con2.jpg)

## 操作界面

+ **图形用户接口**：窗口、图标、菜单、按钮、鼠标（消息、事件）

+ **操作命令**（普通命令）

  在控制台环境下接受键盘输入的命令

+ **批处理与脚本程序**

  在控制台环境下自动处理一批命令

  + Windows批处理程序
  + Linux Shell脚本程序

### Shell

Shell是操作系统与用户交互的界面

+ Shell表现为通过控制台执行用户命令的方式
+ Shell本身不执行命令，仅仅是组织和管理命令

主要功能：...... 、**重定向与管道**、**Shell Script脚本编程**

### 重定向与管道

+ 标准输入输出
  + 命令的输入缺省来自“键盘（文件0）”
  + 命令的输出（含错误）缺省送往“显示器（文件1,2）”

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221003_con3.jpg)

+ 重定向操作

  把命令缺省的输入来源或输出方向修改为其他文件/设备

  ![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221003_con4.jpg)

+ 管道
  + 特殊的重定向操作,程序的输出作为另一个程序的输入
  + 管道操作符$|$
    + “|”符用于连接左右两个命令，将“|”左边命令的执行结果（输出）作为“|”右边命令的输入
    + 在同一条命令中可以使用多个“|”符连接多条命令

### Shell脚本

脚本（Script）通过类似程序的方式执行具有一定逻辑顺序的命令序列完成较复杂的功能和人机交互。

+ 脚本程序保存在**文本文件**中
+ 脚本程序是Shell命令语句的集合
+ 所有命令逐行执行（按逻辑）
+ 凡能shell中直接执行的命令，都可以在脚本中使用
+ 脚本中还可以使用一些不能在shell下直接执行的语句

Bash不区分变量类型

+ 本质上，Bash变量都是**字符串**
+ 当变量值中仅有**数字**时，即为**整形**

运行脚本程序的三个方法

+ 直接运行（用缺省版本的Shell运行脚本程序）
+ 使用某个特定版本的Shell执行脚本
+ 在脚本文件首行指定Shell



## 系统调用

操作系统**内核**为应用程序提供的一系列**服务/函数**（printf、exit、fopen、fgetc...）

+ 一般涉及核心资源或硬件的操作
+ 系统调用运行于**核态**
+ 系统调用过程会产生**中断**：自愿中断
+ 系统调用数量众多

### 系统调用的实现形式

调用N号系统调用，使用指令：SVC N

+ N：系统调用的编号
+ SVC：SuperVisor Call，访管指令
+ SVC是中断指令

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221003_con5.jpg)

### 具体OS中系统调用的实现

+ DOS：**INT 21H**

  利用**AH寄存器**存放系统调用的编号

+ Linux：**INT 80H**
  利用**EAX寄存器**存放系统调用的编号
  + 显示调用：INT 80H
  + 隐式调用：pintf、exit...在高级语言中使用（包含INT 80H中断指令）

INT XXH=SVC指令

AH/EAX=系统调用的编号：N

### Linux系统调用的实质

+ 系统调用是Linux内核的出口
+ 系统调用通过软中断(INT 80H)向内核发出服务请求
+ 系统调用采用API方式向用户提供，遵循POSIX标准

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221003_con6.jpg)

系统调用编号的声明。格式：$\#define\_NR\_CallName~~ID$

系统调用函数的声明。格式：$.long~sys\_XXXX$

系统调用函数的定义。格式：$asmlinkage~int~sys\_mycall()$

#### 系统调用函数的调用方法

直接调用（FuncName不带sys_前缀）

$type=syscall(\_NR\_funcname,arg1,arg2,...)$