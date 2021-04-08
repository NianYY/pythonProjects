import numpy as np
import matplotlib.pyplot as plt


class People(object):
    def __init__(self, count=1000, first_infected_count=3):
        self.count = count
        self.first_infected_count = first_infected_count
        self.init()

    def init(self):
        self._people = np.random.normal(0, 100, (self.count, 2))
        self.reset()

    def reset(self):

        self._round = 0

        self._status = np.array([0] * self.count)

        self._timer = np.array([0] * self.count)

        self.random_people_state(self.first_infected_count, 1)

    def random_people_state(self, num, state=1):

        """随机挑选人设置状态"""
        assert self.count > num

        # TODO：极端情况下会出现无限循环

        n = 0

        while n < num:

            i = np.random.randint(0, self.count)

            if self._status[i] == state:

                continue

            else:

                self.set_state(i, state)

                n += 1

    def set_state(self, i, state):

        self._status[i] = state

        # 记录状态改变的时间

        self._timer[i] = self._round

    """通过状态值，就可以过滤出人群，每个人群都是 people 的切片视图。这里 numpy 的功能相当强大，只需要非常简洁的语法即可实现:"""

    @property
    def healthy(self):

        return self._people[self._status == 0]

    @property
    def infected(self):

        return self._people[self._status == 1]

    @property
    def confirmed(self):
        return self._people[self._status == 2]

    @property
    def dead(self):
        return self._people[self._status == 3]

    @property
    def cured(self):
        return self._people[self._status == 4]


    """按照既定的思路，我们先来定义每轮迭代要做的动作:"""

    def update(self):

        """每一次迭代更新"""

        self.change_state()

        self.affect()

        self.move()

        self._round += 1

        self.report()

    """顺序和开始分析的略有差异，其实并不是十分重要，调换它们的顺序也是可以的。
    
    如何改变状态
    
    这一步就是更新状态数组 self._status 和 计时器数组 self._timer:"""

    def change_state(self):

        dt = self._round - self._timer
        # 16%
        outbreak = self.random_switch(-1+(dt-15)/15)
        # 必须先更新时钟再更新状态
        self._timer[(self._status == 1) & ((dt > 14) | (outbreak == 1))] = self._round
        self._status[(self._status == 1) & ((dt > 14) | (outbreak == 1))] += 1
        #1.5%
        death = self.random_switch(-2.6)
        self._timer[(self._status == 2) & (death == 1)] = self._round
        self._status[(self._status == 2) & (death == 1)] += 1

        #3%
        cure = self.random_switch(-1.88)
        self._timer[(self._status == 2) & (death == 0) & ((dt > 20)|(cure==1))] = self._round
        self._status[(self._status == 2) & (death == 0) & ((dt > 20)|(cure==1))] += 2

        self._timer[(self._status == 4) & (dt > 50)] = self._round
        self._status[(self._status == 4) & (dt > 50)] = 1


    """仍然是通过切片过滤出要更改的目标，然后全部更新。
    
    这里具体的实现我写的非常简单，没有引入太多的变量：
    
    在一定周期内的 感染者(infected)，状态置为 确诊(confirmed)。 我这里简单假设了确诊者就被医院收治，所以失去了继续感染他人的机会(见下面)。如果要搞复杂点，可以引入病床，治愈，死亡等状态。
    
    如何影响他人
    
    影响别人是整个程序的性能瓶颈，因为需要计算每个人之间的距离。
    
    这里继续做了简化，只处理感染者："""

    def infect_possible(self, x=0, safe_distance=3.0):

        """按概率感染接近的健康人

    x 的取值参考正态分布概率表，x=0 时感染概率是 50%（不带口罩）
    x=-0.68 35%的感染率（戴口罩）
    66.7%
    """
        """遍历感染者"""
        for inf in self.infected:
            dm = (self._people - inf) ** 2

            d = dm.sum(axis=1) ** 0.5

            sorted_index = d.argsort()

            for i in sorted_index:

                if d[i] >= safe_distance:
                    break  # 超出范围，不用管了

                if self._status[i] > 0:
                    continue

                """不感染的情况"""
                if np.random.normal() > x:
                    continue

                self._status[i] = 1

                # 记录状态改变的时间

                self._timer[i] = self._round

            """遍历确诊（当确诊即隔离时不需要）
        for inf in self.confirmed:
            dm = (self._people - inf) ** 2

            d = dm.sum(axis=1) ** 0.5

            sorted_index = d.argsort()

            for i in sorted_index:

                if d[i] >= safe_distance:
                    break  # 超出范围，不用管了

                if self._status[i] > 0:
                    continue

                if np.random.normal() > x:
                        continue

                self._status[i] = 1

                # 记录状态改变的时间

                self._timer[i] = self._round"""
    # 可以看到，距离的计算仍然是通过 numpy 的矩阵操作。但是需要对每一个感染者单独计算，所以如果感染者较多，python 的处理效率感人。

    # 如何移动

    """_people 是一个坐标矩阵，只要生成移动距离矩阵 dt，然后它相加即可。我们可以设置一个可移动的范围 width，把移动距离控制在一定范围内。"""

    def move(self, width=2, x=.0):
        """width=10，正常活动范围
        width=2，减小社交范围"""
        movement = self.random_movement(width=width)

        # 限定特定状态的人员移动

        switch = self.random_switch(x=x)

        movement[switch == 0] = 0

        self._people = self._people + movement

        # 这里还需要增加一个控制移动意向的选项，仍然是利用了正态分布概率。考虑到这种场景有可能会重用，所以特地把这个方法提取了出来，生成一个只包含 0 1 的数组充当开关。

    def random_switch(self, x=0.):

        """随机生成开关，0 - 关，1 - 开

    x 大致取值范围 -1.99 - 1.99；

    对应正态分布的概率， 取值 0 的时候对应概率是 50%

    :param x: 控制开关比例

    :return:

    """

        normal = np.random.normal(0, 1, self.count)

        switch = np.where(normal < x, 1, 0)

        return switch

    # 输出结果
    def report(self):

        plt.cla()

        # plt.grid(False)

        p1 = plt.scatter(self.healthy[:, 0], self.healthy[:, 1], s=1)

        p2 = plt.scatter(self.infected[:, 0], self.infected[:, 1], s=1, c='pink')

        p3 = plt.scatter(self.confirmed[:, 0], self.confirmed[:, 1], s=1, c='red')

        p4 = plt.scatter(self.dead[:, 0], self.dead[:, 1], s=1, c='grey')

        p5 = plt.scatter(self.cured[:, 0], self.cured[:, 1], s=1, c='green')

        plt.legend([p1, p2, p3, p4, p5], ['healthy', 'infected', 'confirmed','dead', 'cured'], loc='upper right', scatterpoints=1)

        t = "Round: %s, Healthy: %s, Infected: %s, Confirmed: %s, Dead: %s ,Cured: %s" % \
            (self._round, len(self.healthy), len(self.infected), len(self.confirmed),len(self.dead),len(self.cured))

        plt.text(-200, 400, t, ha='left', wrap=True)

    def affect(self):
        self.infect_possible()

    def random_movement(self, width):
        theta = (np.random.random(self.count)*2-1)*2*np.pi
        mov_y = np.sin(theta)*width
        mov_x = np.cos(theta)*width
        # self._people[:,0]+=mov_x
        # self._people[:,1]+=mov_y
        return np.transpose(np.array([mov_x,mov_y]))


