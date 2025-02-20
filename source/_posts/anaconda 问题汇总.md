---
title: conda 问题汇总
date: 2024-12-16
updated: 2024-12-16
excerpt: conda 问题汇总，如切换默认环境、终端显示问题等
categories: [bug]
tags: [bug,conda,python]
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241216_bg1.jpg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241216_bg1.jpg
---

### 删除环境

```bash
conda remove -n name --all
```

### vscode 终端出现显示两个环境名

这个问题应该是 vscode python 插件自动激活环境和 conda 的自动激活环境之间的不兼容导致的显示问题，解决方法是关闭 conda 的自动激活环境：

```bash
conda config --set auto_activate_base False
```

