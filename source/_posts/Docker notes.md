---
title: Docker 学习笔记
categories: [教程,Docker]
tags: [教程,Docker]
excerpt: Docker 的一些命令和概念
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20240331_bg1.jpg
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20240331_bg1.jpg
---

# 基本概念

1. docker image (映像)：一套提供了应用程序的隔离运行环境的模板；
2. docker container (容器)：一个映像的运行实例（可以类比 image 是类，container 是实例对象），每一个 container 都是独立的运行环境，当容器内没有程序运行时会自动 exit；
# 常用命令
1. docker run [映像名]
   会创建对应映像的一个容器并运行。如果该映像在本地不存在，就会在 https://hub.docker.com/ 中自动查找并下载到本地。
   docker run [映像名] 之后的内容会被识别成要让这个容器中的应用程序执行的命令，如 `docker run ubuntu sleep 100`，会创建并运行 ubuntu 的一个容器并让其睡眠 100 秒。
   当 docker 容器中不再有程序运行时，容器会自动 exit。
   **常用参数** `docker run [option]  [image]  [command]`：（` docker run --help ` 查看全部）
   1. -d：在终端运行 docker run 命令会默认在前台运行该容器，直到 ctrl+c 强制 exit 容器或者在另一个终端 docker stop 。-d 是 detached，标识在后台运行，终端可以继续正尝使用；
   2. --name [name]：设置容器名；
   3. docker run image:tag：tag 代表映像的版本，不写明默认为 latest；各个映像的不同版本对应的 tag 可以在  hub. docker 中查看；
   4. -p [host_port] : [container_port] ：设置端口映射。容器端口只能在 docker host 上通过内部 ip（每个容器都会被分配一个内部 ip，通过 docker inspect 查看） 访问，主机端口可以在外部通过主机 ip 访问，两个端口号可以不同，可以将同一个 container_port 映射到不同的 host_port，但不能反过来；container_port 一般是 docker 运行的应用程序指定的，用户只能配置到主机 port 的映射；
   5. -v [外部路径] : [内部路径]：将容器内的某个目录映射到真实主机上的某个物理路径。默认情况下，当容器 stop 后，容器内部所有的数据都会消失，包括对数据库的操作等等，-v 参数会在对容器内某个目录进行操作时自动映射到指定的外部目录，将数据保存下来，不会随着容器的 stop 而丢失。在下一次 docker run 的时候，这种映射还可以让新的容器读取保存在主机上的数据。
   6. -i：默认情况下，容器不会读取标准输入。这个参数表示将标准输入保持打开状态。-i 是 interactive mode；
   7. -t：表示为容器分配一个伪终端 (pseudo-TTY)。这个选项通常与交互式的容器一起使用，使得用户能够与容器的命令行交互，并且能够获得命令行的控制权。
   8. -it：这是 `-i` 和 `-t` 的结合，用于启动一个既保持标准输入打开又分配了伪终端的交互式容器。这意味着你可以与容器中的命令行交互，并且容器将保持运行状态。
   9. -e [变量名=值]：在运行容器时向容器传递环境变量，供容器内部的程序使用。
   10. --link [内部名] : [容器名] : 用于将不同容器关联起来，形成一套复合的环境。
   11. --cpus=[比例, e.g. .5]：设置该容器可使用的 host 的 cpu 资源的比例上限。
   12. --memory=[大小, e.g. 100 m]：设置该容器可使用的最大内存。
   13. --network=[网络名]：指定该容器运行的网络。
1. docker pull [映像名]
   仅从 hub 中拉取 image，不会直接创建容器并运行。
3. docker ps
   显示目前正在运行中的容器。
4. docker ps -a
   显示目前所有存在的容器，包括运行中和已经退出的。
5. docker stop [容器 id 或 容器名]
   停止运行一个容器，会让容器从 running 状态变为 exited 状态。
   如果是容器名需要全称，如果是容器 id 只需要前 k 位，k 是能够在当前运行的所有容器中唯一标识该容器的最小值，即如果只有一个容器在运行，容器 id 只需要输入第一位就可以。
6. docker rm [容器 id 或容器名]
   彻底删除一个容器，避免继续占用磁盘空间。==在删除前必须先将容器停止运行==。
7. docker images
   显示本地存在的所有映像。
8. docker rmi [映像名]
   删除映像。==在这之前必须关闭并删除该映像的所有容器==。
9. docker exec [容器 id 或容器名]  [command]
   让正在运行中的容器中的应用程序执行命令。
10. docker attach [容器 id 或容器名]
    让在后台运行的容器回到前台，即运行在当前终端。
11. docker inspect [容器 id 或容器名]
    查看某一容器的详细信息。
12. docker logs [容器 id 或容器名]
    查看在后台运行的容器的输出日志。
13. docker image [COMMAND]
    对映像进行操作，如更改标签、删除所有 dangling 映像（没有容器的映像）等等。具体可以通过 `docker image --help` 查看。

# 构建映像
1. 在需要容器化的应用程序目录下创建 Dockerfile 文件，格式如下所示：
```dockerfile
# 该 image 构建于哪个容器之上，以 FROM 开头，每个 Dockerfile 必须指明
FROM Ubuntu

# RUN 开头的命令代表在构建映像时需要执行的命令，包括程序需要用到的依赖、环境等
RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

# COPY 表示将本机的应用程序的源代码拷贝到容器内的哪个位置，格式为 COPY [主机目录] [容器目录]
COPY . /opt/source-code

# ENTRYPOINT 命令表示在 run 容器时需要执行的命令，即应用程序的入口命令
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```
2. 在当前目录执行命令构建映像：`docker build -t [name:tag] .`，-t 指定映像的名字和标签；
3. docker 会默认对 build 过程进行缓存，重新构建时无需担心会从头执行；
4. 使用 `docker images` 命令查看当前存在的映像，构建完成；
5. `docker login` 命令登录 docker hub；
6. `docker push [映像名]` 将构建的映像上传到 docker hub，类似于 github，可以公开下载；
> 如果要上传到 docker hub，映像的名字必须为 `用户名/映像名`，如果不加用户名会默认上传到官方 library ，没有权限会失败。
> 也可以选择上传到其他的私有平台，但需要自己指定域名；甚至可以在本地运行一个 repository 的容器，将自己的映像上传到这上面。具体方法自行查找。
## Dockerfile 中 CMD 和 ENTRYPOINT 的区别与联系
CMD 和 ENTRYPOINT 命令都表示容器运行时执行的命令，它们又都有两种写法，分别是 `CMD/ENTRYPOINT 命令 参数` 和 `CMD/ENTRYPOINT ["命令","参数"]`，一般采用第二种写法。
其中：
1. CMD 会被 `docker run` 命令后携带的命令完全替换，如 `docker run ubuntu sleep 10`，ubuntu 容器就不会执行 Dockerfile 中描述的 `CMD ["bash"]` 命令，而是直接执行 `sleep 10`；
2. ENTRYPOINT 则不会被完全替换，`docker run` 携带的命令会作为参数添加到 ENTRYPOINT 描述的命令后面一同执行。如 `ENTRYPOINT ["sleep"]`，`docker run xxx 10` ，则会执行 `sleep 10`；
3. 如果二者同时出现，那么 CMD 就起到传递参数默认值的作用。如 `ENTRYPOINT ["sleep"]` `CMD ["10"]`，`docker run xxx`，就会执行 `sleep 10`；如果 `docker run xxx 100`，就会替换掉 CMD 中的参数，执行 `sleep 100` 。

# Docker compose
reference: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
当我们需要构建一个复杂的应用程序环境时，我们需要同时运行多个容器并能够将其彼此联系起来，比如有运行数据库的容器，有运行 redis 的容器等等。docker-compose 就是用来整合部署这些不同容器的。
假如不使用 docker compose，我们需要在运行每个容器时手动指定需要与其相关联的其他容器名，用 `docker run --link 内部名1:容器名1 内部名2:容器名2`。
## 使用 docker compose
1. 在项目路径下创建 compose. yaml 文件，格式如下：
```dockerfile
services:
  web: # 容器名
    build: .  # 自动 build image 并运行容器
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"

```
2. 输入命令：`docker compose up`, 这样就可以将文件中指定的容器全部运行并自动进行关联，不需要手动指定。

# Docker engine
1. docker 的数据默认位置是 /var/lib/docker （linux）；
2. `docker volume create [volume name]` 会在 /var/lib/docker/volume 下创建一个名为 volume name 的文件夹。当运行容器时，如果想要将容器内的数据持久化，可以使用 -v 参数：`docker run -v [volume name]:[容器内文件位置]`，就会默认将数据映射到 /var/lib/docker/volume/volume name 中。如果是一个新的 volume name，docker 会自动创建一个新的 volume；
3. 如果不想使用 volume 提供的位置，可以自己手动指定持久化的存储路径 `docker run -v [外部路径] : [内部路径]`，需要显式指明路径；
4. 使用 volume 进行映射叫做 volume mapping，自己指定路径进行映射叫做 bind mapping；
5. 也可以使用 mount 参数进行更加详细的映射设置，比如： `docker run --mount type=bind,source=/host/path,target=/container/path,readonly image_name`

# Docker network
docker 容器运行有三种网络模式：bridge, none, host，默认为 bridge 模式。
1. bridge：桥接模式，会为每一个容器分配一个独立的内部 ip 地址，应用程序运行在内部 ip 内部 port 上，在同一局域网下（比如在主机上）可以直接以 `容器内部 ip: 内部 port` 的方式访问。如果想要从外部访问（假设主机有公网 ip），则需要用 -p 参数映射到主机的某一端口，这样就可以通过 ` 主机 ip: 主机 port ` 的方式访问；
2. host：容器共享主机的网络命名空间，与主机共享相同的 IP 地址和端口。容器没有自己的内部 ip。所以一个特定端口只能够运行一个应用程序，不再区分内部和外部 port，通过 `主机 ip: 主机 port` 访问；
3. none：不与主机进行网络通信。只可以从 `容器内部 ip: 内部 port` 的方式访问，外部无法直接访问容器。
## docker network 操作
1. `docker network create [name] --argument`：创建网络，可以自己设定采用的网络模式、子网范围、网关等等；
2. `docker network --help`：查看所有命令说明；
3. `docker run --network=[network name]`：指定容器运行的网络。

# Docker orchestration
在真正的业务中，我们不只需要在一台 host 上部署一个 docker 容器，而是往往需要在多个主机上同时部署以实现负载均衡等稳定性、安全性要求。有一些 Docker orchestration 工具可以帮助我们方便一键部署，并能够根据业务量动态调整容器数量和其他不同功能。常用的工具有两个：**`docker swarm`** 和 **`kubernetes`**。