'''
action_space && observation_space
'''

import gym
env = gym.make('CartPole-v0')
print(env.action_space)#> Discrete(2)
print(env.observation_space)#> Box(4,)
print(env.observation_space.high)
print(env.observation_space.low)


from gym import spaces
space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}-----手动创建一个离散空间
x = space.sample() #抽样,随机获得0~7中的一个数字
assert space.contains(x)
assert space.n == 8 #断言space空间的个数