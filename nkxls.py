import math
import random
import datetime
import copy
import matplotlib.pyplot as plt
from SimulatedAnnealing.node_generator import NodesGenerator


class SaTSP(object):

    def __init__(self, tf=0.01, alpha=0.9):
        self.tf = tf  # 最低温度
        self.alpha = alpha  # 降温系数
        self.iter_num = []  # 记录迭代次数
        self.distance_path = []  # 记录每一步迭代出来的路径长度
        self.ultimate_path = []
        # 30城市坐标
        self.coordinates = [[41, 94], [37, 84], [54, 67], [25, 62], [7, 64],
                            [2, 99], [68, 58], [71, 44], [54, 62], [83, 69],
                            [64, 60], [18, 54], [22, 60], [83, 46], [91, 38],
                            [25, 38], [24, 42], [58, 69], [71, 71], [74, 78],
                            [87, 76], [18, 40], [13, 40], [82, 7], [62, 32],
                            [58, 35], [45, 21], [41, 26], [44, 35], [4, 50]
                            ]
        # self.coordinates = [[37, 52], [49, 49], [52, 64], [20, 26], [40, 30],
        #                     [21, 47], [17, 63], [31, 62], [52, 33], [51, 21],
        #                     [42, 41], [31, 32], [5, 25], [12, 42], [36, 16],
        #                     [52, 41], [27, 23], [17, 33], [13, 13], [57, 58],
        #                     [62, 42], [42, 57], [16, 57], [8, 52], [7, 38],
        #                     [27, 68], [30, 48], [43, 67], [58, 48], [58, 27],
        #                     [37, 69], [38, 46], [46, 10], [61, 33], [62, 63],
        #                     [63, 69], [32, 22], [45, 35], [59, 15], [5, 6],
        #                     [10, 17], [21, 10], [5, 64], [30, 15], [39, 10],
        #                     [32, 39], [25, 32], [25, 55], [48, 28], [56, 37],
        #                     [30, 40]]
        # self.coordinates = list(NodesGenerator("SimulatedAnnealing/city/eil51.txt").generate())
        self.iteration = 200 * len(self.coordinates)  # 每一个温度过程中迭代次数，马氏链长度

    def initial_temperature(self):  # 温度初始化,采用t0=-delta(f)/(ln0.9)

        dist_list = []
        for i in range(100):  # 生成一百条路径

            path = random.sample(self.coordinates, len(self.coordinates))  # 生成一条随机序列
            dist_list.append(self.all_dist(path))

        t0 = -(max(dist_list) - min(dist_list)) / math.log(0.9)  # 设置初温
        print('初始温度是:', t0)
        return t0

    def D_value(self, current_path, update_path):  # 变换前后目标函数差值

        # print('计算两个状态的差值...')
        current_distance = self.all_dist(current_path)
        # print('当前距离', current_distance)

        update_distance = self.all_dist(update_path)
        # print(update_distance)

        d_value = update_distance - current_distance
        return d_value

    def first_path(self):  # 生成第一条初始化的路径
        length = len(self.coordinates)
        # 因为对初值不敏感，生成一条随机序列, 第一条路径是随机的
        path = random.sample(self.coordinates, length)
        return path

    # 随机交换2个城市顺序，这一步非常重要，调试了五个小时一直不收敛，
    # 深入理解深拷贝和浅拷贝的区别，注意内存中的变化
    def swap(self, path):
        # print('产生新解...')
        city_1 = random.randint(1, len(self.coordinates) - 1)  # 产生第一个交换点
        while True:
            city_2 = random.randint(1, len(self.coordinates) - 1)  # 产生第二个交换点
            if city_2 != city_1:
                break
            else:
                continue
        path[city_1], path[city_2] = path[city_2], path[city_1]
        # print('产生新解结束')
        return path

    # 计算两个点之间的距离
    def two_point_dist(self, point1, point2):

        dist_x = point1[0] - point2[0]
        dist_y = point1[1] - point2[1]
        dist = dist_x ** 2 + dist_y ** 2
        dist = math.sqrt(dist)
        return dist

    def all_dist(self, path):  # 计算所有点距离，总共30段距离
        sum_cities = 0
        n = len(path)
        for i in range(n - 1):  # 先计算前29段距离
            sum_cities += self.two_point_dist(path[i], path[i + 1])
        sum_cities += self.two_point_dist(path[n - 1], path[0])  # 计算第30个点和第一个点的距离，形成闭环
        return sum_cities

    def city_scatter(self):  # 画出城市分布散点图
        city_x = []
        city_y = []
        for i in self.coordinates:
            city_x.append(i[0])
            city_y.append(i[1])
        plt.scatter(city_x, city_y)
        plt.show()

    def city_plot(self, path):  # 画出最终路径图
        city_x = []
        city_y = []
        for i in path:
            city_x.append(i[0])
            city_y.append(i[1])
        plt.plot(city_x, city_y)
        plt.show()

    def plot_graphic(self):  # 画出路径长度随迭代次数变化曲线图
        plt.plot(self.iter_num, self.distance_path)
        plt.show()

    def main(self):  # 函数式编程，调用其它函数，进入这个大循环

        start_time = datetime.datetime.now()  # 增加时间模块，计算运行时间
        t = self.initial_temperature()  # 调用生成初温函数
        current_path = self.first_path()
        # print(current_path)
        i = 0
        while t > self.tf:  # 终止条件
            iteration_number = 0
            while iteration_number < self.iteration:  # metropolis终止条件
                # a = self.all_dist(current_path)
                temple_path = copy.deepcopy(current_path)  # 建立一个当前路径临时列表，防止改变当前路径值
                update_path = self.swap(temple_path)
                # print(update_path)
                de2 = self.D_value(current_path, update_path)
                # print(de,de2)

                if de2 < 0:  # 如果增量为负值，则接受

                    current_path = update_path
                    # print(current_path)

                else:  # 产生新解比较
                    p = math.exp(-de2 / t)
                    if random.random() <= p:
                        current_path = update_path
                        # print(current_path)

                    else:  # 否则保留当前解解，而不是一直产生新解比较，注意误区
                        current_path = current_path
                        # else:
                iteration_number += 1

            t = self.alpha * t

            i = i + 1
            self.iter_num.append(i)
            self.ultimate_path = current_path
            distance = self.all_dist(current_path)
            self.distance_path.append(distance)  # 路径长度存入列表
            # print(distance)

        end_time = datetime.datetime.now()
        this_time = end_time - start_time
        print('程序运行时间：', this_time)

        self.city_scatter()
        self.city_plot(self.ultimate_path)


s1 = SaTSP()

s1.main()
