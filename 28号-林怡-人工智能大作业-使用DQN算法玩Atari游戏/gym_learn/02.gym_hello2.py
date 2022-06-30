import gym
env = gym.make('CartPole-v0')
for i_episode in range(20): # 玩20次游戏
    observation = env.reset()
    for t in range(100): # 一般不会超过100才over,真要超过调参即可
        env.render()#把这段注掉就不会显示画面了,在后台运行不阻塞,运行效率会更高一点
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done: # 判断是否结束 ,如果结束就在工作台上打印结束信息
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()