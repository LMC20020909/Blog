---
title: CSAPP阅读札记——第二章
excerpt: 第二章——信息的表示和处理
categories: [札记, CSAPP]
tags: [札记, CSAPP]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230315_bg3.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230315_bg3.jpg
---

## 字长的概念

***字长***指明指针数据的标称大小，指针的大小就等于字长。

对一个字长为$\omega$的机器而言，虚拟地址的范围为$0\sim2^\omega - 1$，程序最多访问$2^\omega$个字节。

对于32位机，最大虚拟地址空间为$2^{32}-1$个字节，即4GB；对于64位机，最大虚拟地址空间为$2^{64}-1$个字节，即16EB。

> 计算机存储大小单位：
>
> 1KB（Kilo Byte） = $2^{10}$B
>
> 1MB（Mega Byte）= $2^{10}$KB
>
> 1GB（Giga Byte）= $2^{10}$MB
>
> 1TB（Trillion Byte）= $2^{10}$GB
>
> 1PB（Peta Byte）= $2^{10}$TB
>
> 1EB（Exa Byte）= $2^{10}$PB
>
> 1ZB（Zetta Byte）= $2^{10}$EB
>
> 1YB（Yotta Byte）= $2^{10}$ZB
>
> 1BB（Bronto Byte）= $2^{10}$YB

大多数64位机器可以运行为32位机器编译的程序。

### C语言数据类型大小（32位/64位）

![](https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps//img/image-20230423175903299.png)


## 小端法和大端法

**小端法（little endian)**：最低有效字节存放在最前面（低地址）

**大端法（big endian)**：最高有效字节存放在最前面（低地址）

## 字符编码

### ASCII字符码

用1个字节表示一个字符。

十进制数字x的ASCII码为$0x3x$，字符串的终止字符表示为$0x00$

### Unicode

使用32位（4个字节）表示字符。

#### UTF-8

**UTF (Unicode Transformation Format)**

变长字符编码，用1到6个字节编码字符，标准ASCII字符还是使用和它们在SCAII中一样的单字节编码，保持一致性。

## C语言位运算

$|$：按位或

$\&$：按位与

$\sim$：按位取反

$\wedge$：按位异或

与0异或不变，与1异或相当于取反，自己异或自己=0

与0置0，与1不变

或0不变，或1置1

## 移位运算

左移不区分逻辑还是算术，通通补0；

**逻辑右移**：在左端补0

**算术右移**：在左端补最高有效位的值

> 移位运算的优先级很低，加减法的优先级高于移位运算，所以求中点可以写成mid = l + r >> 1;

## 整数编码

### 无符号数编码

$$
B2U_w(\vec{x})=\sum_{i=0}^{\omega-1}x_i2^i
$$

B2U：Binary to Unsigned

> $\omega$位的二进制无符号数，所能表示的范围为$[0, 2^\omega-1]$

### 补码编码

对向量$\vec{x}=[x_{\omega-1}, x_{\omega-2}, ..., x_0]$，
$$
B2T_\omega(\vec{x})=-x_{\omega-1}2^{\omega-1}+\sum_{i=0}^{\omega-2}x_i2^i
$$

> $\omega$位的二进制补码，所能表示的范围为$[-2^{\omega-1}, 2^{\omega-1}-1]$

## 不同表示之间的转换

*二进制表示不变，只是改变了解释这些位的方式*

### 有符号数转为无符号数

#### 补码$\rightarrow$无符号数

$$
T2U_\omega(x)=
\begin{cases}
	x+2^\omega, & \text{if }x<0 \\
	x, & \text{if }x\geq0
\end{cases}
$$

最靠近0的负数（-1）被映射为最大的无符号数（$2^\omega-1$）

#### 无符号数$\rightarrow$补码

$$
U2T_\omega(u)=
\begin{cases}
	u, & \text{if }u\leq TMax_\omega \\
	u-2^\omega, & \text{if }u>TMax_\omega
\end{cases}
$$

当用printf输出数值时，分别用指示符%d、%u、%x以有符号十进制、无符号十进制和十六进制格式输出一个数字。

> C语言中，如果一个运算数是有符号的而另一个是无符号的，C语言会隐式地将有符号数强制转换为无符号数。

#### int的取值范围

C语言中，int为4字节，32位，故表示范围为$[-2^{31}, 2^{31}-1]$，即[-2147483648, 2147483647]

## 扩展位表示

对于无符号数，采取零扩展；

对于有符号数，采取符号扩展，保持数值不变
$$
-2^{\omega-1}=-2^\omega+2^{\omega-1}=-2^{\omega+1}+2^\omega+2^{\omega-1}=\dots
$$

> C语言中会先进行位扩展再进行表示的转换。
>
> 如：
>
> ```c
> short sx = -12345;
> unsigned uy = sx;
> printf("uy = %u\n", uy);	// 输出4294954951
> ```
>
> (unsigned) sx等价于(unsigned) (int) sx，先转为int再转为无符号数
>
> 如果先转为unsigned，再转为int，则最终结果为$2^{16}-12345=53191$

## 截断位表示

将一个$\omega$位的数$\vec{x}=[x_{\omega-1},x_{\omega-2},...,x_0]$截断为一个k位数字，丢弃前$\omega-k$位，得到$\vec{x}'=[x_{k-1},x_{k-2},...,x_0]$

### 截断无符号数

$$
B2U_K[x_{k-1},x_{k-2},...,x_0]=B2U_\omega([x_{\omega-1},x_{\omega-2},...,x_0])~mod~2^k
$$

### 截断补码

$$
B2T_K[x_{k-1},x_{k-2},...,x_0]=U2T_K(B2U_\omega([x_{\omega-1},x_{\omega-2},...,x_0])~mod~2^k)
$$

> 先转为无符号数，再mod $2^k$，之后再转为补码
