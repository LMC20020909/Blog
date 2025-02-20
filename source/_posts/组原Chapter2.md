---
title: 计算机组成原理第二章笔记 
date: 2022-11-14 16:26:51
updated: 2022-11-14 16:26:51
categories: [课业, 计算机组成原理]
tags: [课业, 计算机组成原理,笔记]
excerpt: 计算机中的数据表示方法 黄浩老师 2022.10.16
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg1.jpeg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg1.jpeg
---

### 求负数补码

1. 逐位求反，末位加一，**符号位的进位舍弃**
2. 扫描法：符号位为1，对真值数据位从右到左顺序扫描，**右起第一个1及其右边的0保持不变，其余各位求反**。

### 移码

移码只用于定点整数的表示，用于表示浮点数的阶码。**移码和补码符号位相反，数值位相同（偏移量为$2^n$时）**。

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221022_con1.png)

补码0的表示唯一，多余的编码100...0在定点小数中表示-1，在定点整数中表示$-2^n$
如在四位整数中，原码最小为1111，表示-7，而**补码1000表示-8**

### 负数的反码、补码、移码比较大小

数值部分越大，真值越大（更靠近0），绝对值越小
如在4位整数中，补码最大负数为1111，真值为-1；最小负数为1000，真值为-8
**移码可以直接比较大小**

### 定点小数

$x=x_0.x_1x_2···x_n$，$x_0$为符号位，$x_1-x_2$称为尾数

### 定点数表示范围

定点小数：$1-2^{-n}\geqslant|x|\geqslant2^{-n}$

定点整数：$2^n-1\geqslant|x|\geqslant1$

### 浮点数表示

$$
N=2^E\times M=2^{\pm e}\times (\pm 0.m)
$$

E(Exponent)：阶码，定点整数

M(Mantissa)：尾数，定点尾数

#### 规格化

使尾数真值的最高有效位为1，即尾数的绝对值大于等于$(0.1)_2$或$(0.5)_{10}$

### IEEE754格式

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221022_con2.png)

32位标准：
$$
SE_1E_2E_3...E_nM_2M_3M_4...M_k
$$

+ S：整个数的符号位，0或1
+ E：阶码，共8位，移码表示（偏移值为127）
+ M：尾数，23位定点规格化正小数，$M_1$固定为1，不表示

真值形式：
$$
x=(-1)^S\times (1.M)\times 2^{E-127}
$$
**127的二进制：01111111**

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221022_con3.png)

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221022_con4.png)

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/content/20221022_con5.png)