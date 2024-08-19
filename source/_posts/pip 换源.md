---
title: pip 换源
updated: 2023-12-23 11:58:01
categories: [教程, python]
tags: [教程, python, pip]
excerpt: 永久换源，一劳永逸
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20231223_bg1.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20231223_bg1.jpg
---

# pip 换源

### 临时

```bash
pip install package-name -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 一劳永逸

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

之后直接 pip install package name 就默认使用国内源