---
title: 算法basic
categories: 算法
tags: [算法]
excerpt: 一些最最basic的东西
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230315_bg1.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230315_bg1.jpg
---

## 解算法题步骤

题目描述$\rightarrow$抽象出模型（应该用什么算法，保证**正确性**和**时间不会超**）

c++评测机一秒钟可以运行$10^8$次，所以要保证时间复杂度$<10^7\sim10^8$



## 由数据范围反推算法复杂度以及算法内容

可以把$2^{10}$想象成$10^3$，那么$2^{3.3}$就等同于$10$

| 数据范围           | 算法复杂度                        | 常见算法                                                     |
| ------------------ | --------------------------------- | ------------------------------------------------------------ |
| $n\leq30$          | 指数级别                          | dfs+剪枝、状态压缩dp                                         |
| $n\leq100$         | $O(n^3)$                          | floyd、dp、高斯消元                                          |
| $n\leq1000$        | $O(n^2)$ or $O(n^2logn)$          | dp、二分、朴素版Dijkstra、朴素版Prim、Bellman-Ford           |
| $n\leq10000$       | $O(n*\sqrt n)$                    | 块状链表、分块、莫队                                         |
| $n\leq100000$      | $O(nlogn)$                        | 各种sort、线段树、树状数组、set/map、heap、拓扑排序、dijkstra+heap、prim+heap、Kruskal、spfa、求凸包、求半平面交、二分、CDQ分治、整体二分、后缀数组、树链剖分、动态树 |
| $n\leq1000000$     | $ O(n)or常数较小的 O(nlogn) 算法$ | 单调队列、 hash、双指针扫描、并查集、kmp、AC自动机<br />常数比较小的 O(nlogn) 的做法：sort、树状数组、heap、dijkstra、spfa |
| $n\leq10000000$    | $O(n)$                            | 双指针扫描、kmp、AC自动机、线性筛素数                        |
| $n\leq10^9$        | $O(\sqrt n)$                      | 判断质数                                                     |
| $n\leq10^{18}$     | $O(logn)$                         | 最大公约数、快速幂、数位DP                                   |
| $n\leq10^{1000}$   | $O((logn)^2)$                     | 高精度加减乘除                                               |
| $n\leq10^{100000}$ | $O(logk×loglogk),k表示位数$       | 高精度加减、FFT/NTT                                          |



## 变量范围

int：$-2147483648\sim2147483647，\pm2\times10^9$

long long：$\pm10^{18}$