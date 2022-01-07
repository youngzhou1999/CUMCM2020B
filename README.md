# CUMCM2020-B
Our solution for CUMCM2020-B: "Across the Desert".

our work: (Chinese Version)

通过建立模型为穿越沙漠的游戏玩家提供各种场景下的行动策略，具体包括以下内容：

1. 在天气已知情况下，通过贪心思想枚举得到MDP完整参数，使用线性规划求解最优策略。
2. 在仅知道当前天气的情况下，利用马尔可夫性，条件概率以及混合天气状态与惩罚因子求解最佳策略。
3. 在多名玩家的情况下，利用合作博弈思想，求解近似纳什均衡。

The paper is [here](https://youngzhou1999.github.io/pdfs/B202018005030.pdf). 

