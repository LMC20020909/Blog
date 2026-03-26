---
title: Python 常用技巧
date: 2026-03-22 20:00
updated: 2026-03-22 20:00
categories: [算法]
tags: [算法, python]
excerpt: 记不住就记下来
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20260322_bg2.jpg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20260322_bg2.jpg
---

### 输入处理（ACM 模式）

最常见的输入方式是 `input()` 函数，功能是读入一整行并去掉行末换行符（行末空格仍保留）。但速度较慢，在大量输入数据时会拖慢程序运行速度。因此一般采用 `sys.stdin.readline()` 来替换原生 `input()`。

- 读整行

  ```python
  import sys
  
  input = sys.stdin.readline
  
  a, b = map(int, input().split())
  print(a + b)
  ```

- 读矩阵

  ```python
  import sys
  
  input = sys.stdin.readline
  
  m, n = map(int, input().split())
  mat = [list(map(int, input().split())) for _ in range(m)]
  ```

- 读字符串

  注意：**sys.stdin.readline() 会将换行符一并读入！**

  读整数和列表不用加 `strip()` 是因为 `split()` 和 `int()` 方法会处理掉多余空格和换行符。

  ```python
  import sys
  
  input = sys.stdin.readline
  
  s = input()
  # print(s) -> "abc\n"
  
  s = input().strip()	# 如果行末空格有意义则需要 s = input().rstrip('\n')
  # print(s) -> "abc"
  ```

- 读到文件末尾 EOF

  ```python
  import sys
  
  for line in sys.stdin:
      nums = list(map(int, line.split()))
      print(sum(nums))
  ```



### 字符串格式化输出

#### strip(), lstrip() 和 rstrip()

#### 控制宽度、前后填充



### 不同方式的取整



### python 内置的几种二阶方法

#### map

#### reduce



### 矩阵操作

#### 矩阵旋转

#### 一次遍历同时记录行列信息

```python
m, n = len(mat), len(mat[0])
row = [0] * m
col = [0] * n
for i in range(m):
    for j in range(n):
        if 满足某条件:
            row[i] += 1
            col[j] += 1
```

#### list(zip(*grid)) 实现矩阵转置



### 列表原地修改

有时候题目要求原地修改某列表，如果我们想偷懒，开新空间处理最后再复制回去的话，那就不能简单地写 `nums1 = nums2`，需要写成 `nums1[:] = nums2`。

```python
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums1 = nums2 # 把 nums1 这一变量名绑定到 [4, 5, 6] 上
nums1[:] = nums2 # 将 [1, 2, 3] 改成 [4, 5, 6]
```



### 找左右两边最大最小值



### 无序数组找中位数

实际上是 Top K 问题

快速选择



### Counter() 可以直接比较大小



### 模运算恒等式

(*a*+*b*)mod*m*=((*a*mod*m*)+(*b*mod*m*))mod*m*

(*a*⋅*b*)mod*m*=((*a*mod*m*)⋅(*b*mod*m*))mod*m*

(*a*−*b*)mod*m*=((*a*mod*m*)−(*b*mod*m*)+*m*)mod*m*

https://leetcode.cn/discuss/post/3584387/fen-xiang-gun-mo-yun-suan-de-shi-jie-dan-7xgu/



### 覆盖子串问题中的判断技巧



### 怎样是“合法括号”字符串？



### 位运算技巧

https://leetcode.cn/discuss/post/3571304/cong-ji-he-lun-dao-wei-yun-suan-chang-ji-enve/
