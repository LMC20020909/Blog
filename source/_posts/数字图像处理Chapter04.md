---
title: 数字图像处理第四章 
updated: 2022-11-14 16:26:51
categories: [课业, 数字图像处理]
tags: [课业, 数字图像处理, 笔记, 复习]
excerpt: 第四章 线性运算与空间图像增强 薛志东老师 2022.10.27
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg7.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20221022_bg7.jpg
---

### 第四章 线性运算与空间图像增强

#### 线性系统

+ 叠加原理：$y_1 = T[x_1], y_2 = T[x_2]\rightarrow y_1+y_2=T[x_1]+T[x_2]=T[x_1+x_2]$
+ 齐次原理：$\alpha y=T[\alpha x]=\alpha T[x]$

$\rightarrow ay_1+by_2=T[ax_1+bx{_2}]$

对于输入信号的加权和的响应等于单个输入信号响应的加权和

#### 移不变系统

如果输入序列移位，则输出序列进行相应的移位

$y(i,j)=T[x(i,j)]\rightarrow y(i-m,j-n)=T[x(i-m,j-n)]$

#### 线性移不变系统

具有移不变系统的线性系统

#### 距离

+ 欧氏距离
+ 街区距离&emsp;&emsp;$d=|x_1-x_2|+|y_1-y_2|$
+ 棋盘距离&emsp;&emsp;$d=max(|x_1-x_2|,|y_1-y_2|)$

#### 图像平滑

##### 均值滤波器

+ 去除图像的不相关细节
+ 会模糊边缘

##### 中值滤波器

+ 用像素邻域内灰度的中值代替该像素的值

+ 很好的处理椒盐噪声

#### 图像锐化

+ 加强图像中景物的边缘和轮廓

+ 用空间微分实现
+ 增强边缘和其他突变（如噪声），削弱灰度变化缓慢的区域

##### 拉普拉斯算子——使用二阶微分

$$
\nabla^2f=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}\\
\frac{\partial^2f}{\partial x^2}=f(x+1,y)+f(x-1,y)-2f(x,y)\\
\frac{\partial^2f}{\partial y^2}=f(x,y+1)+f(x,y-1)-2f(x,y)\\
\nabla^2f(x,y)=f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)-4f(x,y)\\
g(x,y)=f(x,y)-\nabla^2f(x,y)
$$

模板：

| 0    | 1    | 0    |
| ---- | ---- | ---- |
| 1    | -4   | 1    |
| 0    | 1    | 0    |

#### 一阶微分——梯度

$$
\nabla f=grad(f)=[g_x,g_y]^{T}=[\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}]^{T}
$$

梯度的幅度：
$$
G[F(x,y)]=[(\frac{\partial F}{\partial x})^2+(\frac{\partial F}{\partial y})^2]^{\frac{1}{2}}
$$

##### Roberts交叉梯度算子

$$
G(i,j)=|f(i+1,j+1)-f(i,j)|+|f(i+1,j)-f(i,j+1)|
$$



模板：

| -1   | 0    |
| ---- | ---- |
| 0    | 1    |

| 0    | -1   |
| ---- | ---- |
| 1    | 0    |

##### Sobel锐化算法

**强化四邻域**

模板：

| -1   | 0    | 1    |
| ---- | ---- | ---- |
| -2   | 0    | 2    |
| -1   | 0    | 1    |

| -1   | -2   | -1   |
| ---- | ---- | ---- |
| 0    | 0    | 0    |
| 1    | 2    | 1    |

##### Priwitt锐化算法

| -1   | 0    | 1    |
| ---- | ---- | ---- |
| -1   | 0    | 1    |
| -1   | 0    | 1    |

| -1   | -1   | -1   |
| ---- | ---- | ---- |
| 0    | 0    | 0    |
| 1    | 1    | 1    |



