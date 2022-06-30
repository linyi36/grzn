# Reference
[Simple Reinforcement Learning](https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56)
# 个人理解
## What's Q?
Quality
## Steps
1. create a q-table
2. Q-learning and making updates
    代理可以选择的和环境交互的方式有两种:
    (1)使用Q表这一已知信息筛选最合理行为----exploiting
    (2)随即行动--------exploring
    epsilon(ε)就是探索行为占的总比例
    
    making updates指的是修改q-table,发生在每个action之后,结束于某个游戏结尾...