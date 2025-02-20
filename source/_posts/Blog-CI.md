---
title: Blog CI
date: 2024-08-19 17:47:30
updated: 2024-08-19 17:47:30
excerpt: 利用 GitHub Actions 实现博客自动化部署并多端同步
categories: 博客
tags: [博客,github,教程]
index_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20240819_bg1.png
banner_img: https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20240819_bg1.png
---

最近新配了一台主机，加上 macbook 和老笔记本一共就有了三台设备。俗话说得好，有新的不用旧的，这个博客的环境和数据都保存在老笔记本上，每次想发点什么东西还要特意打开它，十分麻烦。加上三台电脑一般被我放在三个地方，于是就有了随时随地写、随时随地发的需求。本来想的是将博客移植到新主机上面去，但在搜索攻略的时候发现有一种能够免配环境、自动部署、多端同步的处理方式正合我意，毕竟出于需求隔离的想法，暂时还不是很想对另外两台设备动过多的手脚。

通俗来讲，这种方式之所以有效，本质上是相当于把原来在电脑本地配置安装的 hexo 博客环境和数据转移到 github 的服务器上，这样就不用在本地安装 NodeJS 和 hexo 环境。同时编写一个自动化脚本，利用 github actions 功能，每当博客的源代码有更新时自动编译，并将静态文件推送到 github.io 的仓库中。

### 建仓

为了实现这一需求，我们需要准备两个 github repo，一个用来存放博客的源代码，一个用来存放网页的静态文件。如果你在本地已经使用过博客，那么后一个仓库，也就是你的 username.github.io 仓库，应该已经准备好了，在此不再赘述；前一个 repo 我起名为 Blog，设置为 private（毕竟是存放源码的地方，需要考虑隐私性）。建好之后，就可以将你在本地的博客源代码一个不剩的全部 push 上去了。注意是把整个根目录都推送上去，包括博客的配置文件等。具体操作如下：

```bash
# 我的本地博客的根目录为 Blog
cd Blog/
git init
git remote add origin xxx
git branch -M main
git add .
git commit -m "xxx"
git push -f origin main
```

在此过程中，可能会出现 git add . 时出错的情况。这是因为在目录下存在着其他 git 仓库，而 git 并不支持嵌套仓库。排查发现是 themes/next 目录是一个 git 仓库。最简单直接的方法就是把 themes/next 目录下的 **.git 文件夹删掉**，这样我们的主题文件夹就是一个普通的目录，而不是一个 git 仓库，这样嵌套仓库的内容就会成为当前仓库内容的一部分，就可以使用 git add 对这些文件进行跟踪。这样做的代价就是无法自动更新主题，但实际上主题的更新与博客的内容无关，且周期很长，所以无伤大雅。删掉之后重新 add commit push 就可以了。

### 赋予权限

在此之后，我们需要赋予这个 Blog 仓库向另一个仓库（github.io）推送代码的权限。你可以把这个存放着博客源代码的仓库当作一个云端服务器，每次向它 push 代码就相当于在这个 server 上编译博客并向 github.io 推送，所以就像我们在本地使用 git 一样，需要有权限访问更改你的 repo。

在 Github 中这种权限验证方式有三种：

1. 用户名密码，最古早的方式，在2021年就基本已被弃用；
2. SSH 密钥验证，目前最主要的方式，只要公钥存放在你的 Github 账户里，拥有对应私钥的一方就拥有了访问更改你仓库的权限；
3. Token 链接，与 SSH 相比，好处是你可以对每个 token 的权限进行更加细化的设置，如访问、更改、删除等，坏处是 token 的验证是单向的，而我们一般为了图方便都会给 token 赋予最高权限，换句话说，拥有了你的 token 的一方相当于掌握了你的密码，安全性难以保证。

当然，为了赋予 Blog 仓库权限，我们无论是使用 SSH 还是 Token，都需要把一个有权限的 SSH 私钥或是 token 上传到云端，似乎安全性都无法保证。但实际上，GitHub 提供了在仓库中设置机密（Secrets）的功能，允许将敏感信息（如 token 或 密钥）安全地存储并在工作流中使用。GitHub 通过加密和访问控制来保护这些机密，避免在构建过程中泄露。使用 SSH 验证只需要上传私钥就行，而使用 Token 还需要对博客的配置文件中的 deploy 地址进行更改。基于最小化实现原则，本人选择了 SSH 的方式。具体操作如下：

1. 找一个已有的有效密钥，即公钥已经添加到了你的 Github 设置中。如果没有或者不想重用的话，可以再新生成一个然后将公钥添加好：
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```

2. 将私钥添加到 Blog 仓库中：
   ![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191908522.png)

	这里我取名为 HEXO_DEPLOY_PRIVATE_KEY_DELL_RSA。注意，在复制私钥的时候一定要全体复制，直接 ctrl A + ctrl C，否则可能会因格式不对而无法验证权限。

### 添加 GitHub Actions 脚本

你可以把 GitHub Actions 功能当作触发器，当你设定的某个条件满足时出发相应的动作。我们的需求是当博客更新 push 时，自动编译并部署。所以在这里触发器的条件就是主分支有新的 push，触发的动作就是配置 hexo 博客环境并编译部署，也就是之前我们在本地做的那一套。

点击 Blog 仓库的 `Actions`。

![image-20240819192224011](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191922048.png)

点击 `New workflow`。

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191923074.png)

点击 `set up a new workflow yourself`。

![](https://gcore.jsdelivr.net/gh/LMC20020909/BlogMaps2@main//img/202408191924277.png)

编写触发器脚本，脚本是一个 yml 文件。本人的脚本如下：

```yaml
# workflow name
name: Hexo Blog CI

# main branch on push, auto run
on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      # check it to your workflow can access it
      # from: https://github.com/actions/checkout
      - name: Checkout Repository
        uses: actions/checkout@v2
      #   with:
      #     fetch-depth: 0

      # - name: Restore file modification time
      #   run: |
      #     git config --global core.quotepath false
      #     find source -name '*.md' | while read file; do touch -d "$(git log -1 --format="@%ct" "$file")" "$file"; done

      # from: https://github.com/actions/setup-node
      - name: Setup Node.js
        uses: actions/setup-node@main

      - name: Setup Hexo Dependencies
        run: |
          npm install hexo-cli -g
          npm install

      - name: Setup Deploy Private Key
        env:
          HEXO_DEPLOY_PRIVATE_KEY: ${{ secrets.HEXO_DEPLOY_PRIVATE_KEY_DELL_RSA }}
        run: |
          mkdir -p ~/.ssh/
          echo "$HEXO_DEPLOY_PRIVATE_KEY" > ~/.ssh/id_rsa 
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan github.com >> ~/.ssh/known_hosts

      - name: Setup Git Infomation
        run: |
          git config --global user.name 'xxx' 
          git config --global user.email 'xxx'

      - name: Deploy Hexo
        run: |
          hexo clean
          hexo generate 
          hexo deploy

```

以下解释来自于 ChatGPT：

> 这是一个使用 GitHub Actions 实现 Hexo 博客持续集成（CI）的脚本。下面是对每个部分的详细解释：
>
> **1. Workflow 名称**
>
> ```yaml
> name: Hexo Blog CI
> ```
> 这部分为工作流命名为 "Hexo Blog CI"，表示这是用于 Hexo 博客的持续集成工作流。
>
> **2. 触发条件**
>
> ```yaml
> on:
> push:
>  branches:
>       - main
> ```
> 这个部分定义了工作流的触发条件。它会在推送到 `main` 分支时自动运行。这意味着每当你向 `main` 分支提交更改时，工作流都会被触发。
>
> **3. Jobs 部分**
>
> ```yaml
> jobs:
>   build:
>     runs-on: ubuntu-latest
> ```
> `jobs` 部分定义了实际运行的任务。这里定义了一个名为 `build` 的任务，使用的是 `ubuntu-latest` 环境。
>
> **3.1 检出仓库**
>
> ```yaml
> - name: Checkout Repository
>   uses: actions/checkout@v2
> ```
> 这一步使用 `actions/checkout@v2` 检出你的 GitHub 仓库代码。这使得工作流能够访问并操作你项目的代码。
>
> **3.2 设置 Node.js 环境**
>
> ```yaml
> - name: Setup Node.js
>   uses: actions/setup-node@main
> ```
> 这一步使用 `actions/setup-node@main` 设置 Node.js 环境，确保工作流可以使用 Node.js 运行 Hexo 命令。
>
> **3.3 安装 Hexo 依赖项**
>
> ```yaml
> - name: Setup Hexo Dependencies
>   run: |
>     npm install hexo-cli -g
>     npm install
> ```
> 这一部分通过 `npm` 安装 Hexo 命令行工具和项目依赖项。这一步为 Hexo 的生成和部署提供了必要的环境。
>
> **3.4 设置部署私钥**
>
> ```yaml
> - name: Setup Deploy Private Key
>   env:
>     HEXO_DEPLOY_PRIVATE_KEY: ${{ secrets.HEXO_DEPLOY_PRIVATE_KEY_DELL_RSA }}
>   run: |
>     mkdir -p ~/.ssh/
>     echo "$HEXO_DEPLOY_PRIVATE_KEY" > ~/.ssh/id_rsa 
>     chmod 600 ~/.ssh/id_rsa
>     ssh-keyscan github.com >> ~/.ssh/known_hosts
> ```
> 此步骤用于配置 SSH 私钥，以便工作流能够通过 SSH 连接到 GitHub，并将生成的内容推送到你的博客仓库中。密钥保存在 GitHub Secrets 中，以确保安全性。
>
> **3.5 配置 Git 用户信息**
>
> ```yaml
> - name: Setup Git Infomation
>   run: |
>     git config --global user.name 'xxx' 
>     git config --global user.email 'xxx'
> ```
> 这一步配置了 Git 用户名和邮箱信息，确保在部署过程中 Git 提交有正确的用户信息。
>
> **3.6 部署 Hexo**
>
> ```yaml
> - name: Deploy Hexo
>   run: |
>     hexo clean
>     hexo generate 
>     hexo deploy
> ```
> 最后一步执行了 Hexo 的一系列命令：
> - `hexo clean` 清理旧的生成文件。
> - `hexo generate` 生成静态文件。
> - `hexo deploy` 将生成的文件部署到远程服务器（通常是 GitHub Pages）。
>
> **总结**
>
> 通过上述工作流脚本，你可以在每次推送到 `main` 分支时自动生成和部署 Hexo 博客。这使得博客的更新变得自动化和更加便捷。

最后点击提交 commit 即可。

别忘了在本地 git pull 将其同步在本地更新。

到此大体工作基本结束。以后只需要在本地编写 markdown 文件并 push 到仓库中，博客就会同步更新了。在另外的设备上也是同理，将 Blog 仓库 clone 下来，进行更改，再进行 push，完全不需要在本地安装配置 hexo 的环境。

注意，多端同步主要依靠每次更新后在另外的设备上的 git pull 操作，所以无论使用哪台电脑，在进行更改之前最好先 git pull 一下。

### 常见问题

#### 域名绑定问题

如果你的 github.io 像我一样绑定了自定义域名，那么根据我在网上看到的教程，还需要进行额外一步操作：

1. 在博客根目录的配置文件（_config.yml）中找到`skip_render`字段，添加值`'CNAME'`：
   ```yaml
   skip_render: 'CNAME'
   ```

2. 在`/source/`目录下创建一个文件，命名为`CNAME`，里边的内容写你的域名。只写域名即可。例如`mingchenliu.com`，不需要添加`http(s)://`。

#### 博客文章发表时间的顺序错乱问题

在上面的步骤都成功了之后，我发现博客文章的展示顺序全部错乱了。由于 hexo 默认按照文章源文件的修改时间从近到远排序，所以我细看之下发现所有文章的发表时间全部变成了 push 到 repo 的时间，导致顺序错乱。按照网上的攻略，有以下两种解决方式：

1. 在所有文章顶部的 metadata 部分（也就是以`---`分割的部分）中添加 `updated`字段，这样 hexo 在渲染排序时就会优先根据这一时间。
2. 在 GitHub Actions 的自动化脚本中进行修改，将文件的修改时间设置为 Git 中最后一次提交的时间戳。

本着最小化实现的原则，我首先尝试了第二种方案。在脚本中添加了几行代码（即前文中注释掉的代码）：

```yaml
# check it to your workflow can access it
# from: https://github.com/actions/checkout
- name: Checkout Repository
  uses: actions/checkout@v2
	with:
    fetch-depth: 0

- name: Restore file modification time
  run: |
    git config --global core.quotepath false
    find source -name '*.md' | while read file; do touch -d "$(git log -1 --format="@%ct" 
```

以下是 ChatGPT 的解释：

> 这些被注释掉的代码片段是工作流中的可选步骤，分别与仓库的检出配置和文件的修改时间恢复有关。以下是对每个部分的解释：
>
> **1. 可选的仓库检出配置**
>
> ```yaml
> #   with:
> #     fetch-depth: 0
> ```
> 这个部分是 `actions/checkout@v2` 步骤的可选配置项。`fetch-depth: 0` 表示在检出代码时，克隆整个 Git 历史记录，而不仅仅是最新的提交。默认情况下，`actions/checkout` 只会克隆最近的一个提交，以节省时间和带宽。如果你需要访问整个提交历史（例如在运行特定的 Git 命令或生成变更日志时），你可以取消注释这一部分并设置 `fetch-depth` 为 `0`。
>
> **2. 恢复文件的修改时间**
>
> ```yaml
> # - name: Restore file modification time
> #   run: |
> #     git config --global core.quotepath false
> #     find source -name '*.md' | while read file; do touch -d "$(git log -1 --format="@%ct" "$file")" "$file"; done
> ```
> 这一段代码的目的是恢复文件的修改时间，使其与 Git 记录中的最后一次提交时间一致。
>
> - `git config --global core.quotepath false`：这行命令禁用了 Git 中的路径转义，使路径信息在输出时不包含特殊字符的转义形式。
>
> - `find source -name '*.md'`：这行命令查找 `source` 目录下所有以 `.md` 结尾的文件（即 Markdown 文件）。
>
> - `while read file; do touch -d "$(git log -1 --format="@%ct" "$file")" "$file"; done`：这段代码循环遍历查找到的每个文件，使用 `touch -d` 命令将文件的修改时间设置为 Git 中最后一次提交的时间戳（`@%ct`）。
>
> 这一部分的作用是在一些情况下保持文件的修改时间与 Git 提交历史一致，可能对 Hexo 的文件生成逻辑有影响。如果 Hexo 或其他系统依赖于文件的修改时间来决定是否更新某些内容，这一步可能是必要的。
>
> **总结**
>
> 这些被注释的代码片段是为了在特定需求下更灵活地配置工作流。如果你需要完整的 Git 历史或准确的文件修改时间戳，可以考虑取消注释并使用这些选项。

然而这对我并没有用，时间信息并没有恢复。于是我尝试了第一种方式，为所有的文章添加一个 `updated`字段，标识文件的修改时间。当然，这一步需要在老电脑上操作，因为这些文件的基础信息保存在最初的系统上，而在新电脑上 clone 下来的文件的修改时间都是 clone 的时间。

另外，出于个人偏好，我喜欢让文章根据创建时间而不是修改时间进行排序，这样在我对之前的文章内容进行修改后不会影响排序。所以在添加时我获取了文件的创建时间添加到字段中。

这一操作是通过编写一个简单的 python 脚本完成的。但在添加好之后重新 push 竟然没有任何效果。在查阅文档和反复试验后我发现，可能是由于本人使用的主题或者配置的原因，我的文章发表时间优先设置为文章的`Date`字段的值而非`updated`字段，如果没有该字段则获取文件的系统信息（也就是 git 无法获取到的时间）。就是因为 GitHub 将后者设置成了最新 push 的时间，所以才导致了这一问题。

由此我又为所有文章添加了一个`Date`字段，值为文件的创建时间，这倒是阴差阳错和我的需求统一起来，算是“名实相符”了。

> 子路曰：「衛君待子而為政，子將奚先？」子曰：「必也正名乎！」子路曰：「有是哉，子之迂也！奚其正？」子曰：「野哉由也！君子於其所不知，蓋闕如也。名不正，則言不順；言不順，則事不成；事不成，則禮樂不興；禮樂不興，則刑罰不中；刑罰不中，則民無所措手足。故君子名之必可言也，言之必可行也。君子於其言，無所苟而已矣。」

果然，名正言顺则事可成。这个问题算是解决了。

最后附上批处理为所有文章添加`Date`字段的 python 代码（需要放在文章的源文件的目录下执行，在我这里是 `source/_posts/`）：

```python
import os
from datetime import datetime


def creation_time_extraction(file_path):
    # 获取文件的创建时间 (Windows 和部分类Unix系统)
    creation_time = os.path.getctime(file_path)

    # 转换为可读的日期时间格式
    creation_time_readable = datetime.fromtimestamp(
        creation_time).strftime('%Y-%m-%d %H:%M:%S')

    return creation_time_readable


def update_md(file_path, creation_time):
    with open(file_path, "r", encoding="utf-8") as md_file:
        content = md_file.readlines()

    start_idx, end_idx = None, None
    for i, line in enumerate(content):
        if line.strip().startswith("---"):
            if start_idx is None:
                start_idx = i
            else:
                end_idx = i
                break

    if start_idx is not None and end_idx is not None and start_idx + 1 < end_idx:
        for i in range(start_idx + 1, end_idx):
            if content[i].strip().startswith("title:"):
                content.insert(i + 1, f"date: {creation_time}\n")
                break

        with open(file_path, "w", encoding="utf-8") as md_file:
            md_file.writelines(content)

        return True

    return False


def main():
    files = [f for f in os.listdir('.') if f.endswith('.md')]

    n = len(files)
    m = 0

    for file_name in files:
        file_path = os.path.join(os.getcwd(), file_name)
        creation_time = creation_time_extraction(file_path)
        # print(f"File: {file_name}, Created: {creation_time}")
        flag = update_md(file_path, creation_time)
        if not flag:
            m += 1
            print(file_path)

    print("total num of files: ", n)
    print("fail updating num: ", m)


if __name__ == "__main__":
    main()

```

### 参考文章

1. https://cloud.tencent.com/developer/article/1611808
2. https://cloud.tencent.com/developer/article/2369534
3. https://www.cnblogs.com/yyyzyyyz/p/15792199.html

