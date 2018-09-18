# 贪心算法
class Knapsack_problem():
    #weight：物品重量  price:物品对应的价格
    #totalC：背包最大承载重量
    def __init__(self, weight, price, totalC):
        self.weight = weight
        self.price = price
        self.number = len(weight)
        #status：物品状态，0-未选择，1-已选中，2-已判断不能再选择
        #初始化物品状态为未选择状态
        self.status = [0]*self.number
        self.totalC = totalC

    #打印所有选中的物品信息，以及所有物品总重量及总价格
    def PrintResult(self):
        totalW = 0
        totalP = 0
        for i in range(self.number):
            if self.status[i] == 1:
                totalW += self.weight[i]
                totalP += self.price[i]
                print('所选物品：%d, 重量：%d, 价格:%d' % (i, self.weight[i], self.price[i]))
        print('所选物品总重: %d, 总价值: %d' % (totalW, totalP))

    #贪婪算法
    def GreedyAlgorithm(self):
        nCurWeight = 0#已选中的物品重量
        while True:
            idx = self.ChooseFunc1()
            if idx == -1:
                break
            #如果已选中的物品重量 + 欲选择的物品重量 < 背包允许最大重量
            if nCurWeight + self.weight[idx] <= self.totalC:
                self.status[idx] = 1
                nCurWeight += self.weight[idx]
            else:
                self.status[idx] = 2
        self.PrintResult()

    #贪婪策略1：每次选择价格最高的物品
    def ChooseFunc1(self):
        maxPrice = 0
        index = -1
        for i in range(self.number):
            if (self.status[i] == 0) and (self.price[i] > maxPrice):
                maxPrice = self.price[i]
                index = i
        return index
    #贪婪策略2：每次选择重量最轻的物品
    def ChooseFunc2(self):
        minWight = 10000
        index = -1
        for i in range(self.number):
            if (self.status[i] == 0) and (self.weight[i] < minWight):
                minWight = self.weight[i]
                index = i
        return index
    #贪婪策略3：每次选择价格密度最高的物品
    def ChooseFunc3(self):
        index = -1
        maxDensity = 0
        for i in range(self.number):
            if self.status[i] == 0:
                den = self.price[i]/self.weight[i]
                if den > maxDensity:
                    maxDensity = den
                    index = i
        return index


if __name__ == '__main__':
    weight = [35, 30, 60, 50, 40, 10, 25]
    price = [10, 40, 30, 50, 35, 40, 30]
    totalC = 150
    instance = Knapsack_problem(weight, price, totalC)
    instance.GreedyAlgorithm()