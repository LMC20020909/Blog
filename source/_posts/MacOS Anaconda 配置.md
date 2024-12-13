---
title: MacOS conda 创建环境时的特殊配置
date: 2024-12-13
updated: 2024-12-13
excerpt: MacOS conda 创建环境时的特殊配置
categories: bug
tags: [bug,conda,python]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241212_bg1.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20241212_bg1.jpg
---

在 Mac 系统上使用 Anaconda 时，如果直接使用 `conda create` 命令创建环境会默认环境为 osx-64，即原本 Intel / AMD 芯片的 x86_64 架构。但对于 M 系列这种 arm64 架构的芯片来说，在使用时可能会出现配置上的问题。例如，在 `import torch` 时，可能会出现类似这样的信息：

```bash
Intel MKL WARNING: Support of Intel(R) Streaming SIMD Extensions 4.2 (Intel(R) SSE4.2) enabled only processors has been deprecated. Intel oneAPI Math Kernel Library 2025.0 will require Intel(R) Advanced Vector Extensions (Intel(R) AVX) instructions.
```

因此需要将环境更改为 osx-arm64.

### 查看当前环境的 Python 包架构

在激活环境后运行以下命令：

```bash
python -c "import platform; print(platform.machine())"
```

或者 `conda info` 查看 `platform` 字段的值



### 创建时设置环境架构

在创建环境时，使用以下命令：

```bash
CONDA_SUBDIR=osx-arm64 conda create -n envname
```

或者

```bash
conda create --platform osx-arm64 -n envname
```



### 更改当前环境的架构设置

```bash
conda config --env --set subdir osx-arm64
```

