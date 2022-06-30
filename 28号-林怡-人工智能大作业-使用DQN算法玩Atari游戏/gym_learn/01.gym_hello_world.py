'''
https://github.com/openai/gym
这段代码来源于: https://gym.openai.com/docs/
'''

import gym

env = gym.make('MountainCar-v0')
env.reset() # 初始化;启动
for _ in range(1000): # 决定游戏画面显示的帧数
    env.render() # 渲染
    env.step(env.action_space.sample())  # take a random action
    # In fact, step returns four values. These are:observation (object),reward (float),done (boolean) and info (dict):
env.close()
