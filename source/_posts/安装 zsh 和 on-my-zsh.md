---
title: 安装 zsh 和 oh-my-zsh
date: 2025-11-21 20:36:00
updated: 2025-11-21 20:36:00
categories: [教程, server]
tags: [教程, server, zsh, oh-my-zsh]
excerpt: 有/无 root 权限安装 zsh 和 oh-my-zsh
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20260315_bg2.jpg
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20260315_bg2.jpg
---

### 安装 zsh 和 oh-my-zsh

1. 无 root 权限安装 zsh

   ```
   cd ~
   wget https://sourceforge.net/projects/zsh/files/latest/download -O zsh.tar.xz
   tar xf zsh.tar.xz
   cd zsh-*
   ./configure --prefix=$HOME/.local
   make -j$(nproc)
   make install
   ```

   zsh 安装在 ~/.local/bin/zsh

2. 自动进入 zsh

   在 .bashrc 中输入：

   ```bash
   export PATH=$HOME/.local/bin:$PATH
   # 自动切换到 zsh（避免死循环）
   if [ -t 1 ] && [ -x "$HOME/.local/bin/zsh" ] && [ -z "$ZSH_VERSION" ]; then
       exec $HOME/.local/bin/zsh
   fi
   ```

   打开 bash 后自动切换到 zsh

   输入 `zsh --version`，显示版本号即安装成功。

3. 安装 oh-my-zsh

   在 zsh 中输入安装命令：

   curl:

   ```bash
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   ```

   wget:

   ```bash
   sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
   ```

   安装完成！

