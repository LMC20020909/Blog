---
title: flappy-bird-gym环境安装
updated: 2023-07-21 10:41:31
categories: [教程, RL]
tags: [教程, RL, gym]
index_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230428_bg3.png
banner_img: https://cdn.jsdelivr.net/gh/LMC20020909/BlogMaps@main/bg/20230428_bg3.png
---
如题
<!--more-->

```bash
conda create -n flappy-bird-gym python=3.8
```

```bash
pip install setuptools==65.5.0	//需要降低版本，不然无法安装低版本的gym
```

```bash
pip install gym=0.18.0	//安装0.18.x版本的gym
```

```bash
pip install flappy-bird-gym
```

```python
import time
import flappy_bird_gym
env = flappy_bird_gym.make("FlappyBird-v0")

obs = env.reset()
while True:
    # Next action:
    # (feed the observation to your agent here)
    action = ...  # env.action_space.sample() for a random action

    # Processing:
    obs, reward, done, info = env.step(action)
    
    # Rendering the game:
    # (remove this two lines during training)
    env.render()
    time.sleep(1 / 30)  # FPS
    
    # Checking if the player is still alive
    if done:
        break

env.close()
```

运行成功
