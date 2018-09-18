# 1.编写一个银行卡类，具有账号，人名与余额属性。编写提款机类，接收一张银行卡，
# 并且具有存款，提款，查询余额，转账功能。
import time
import random

class BankCard():
    def __init__(self,idCard,name,balance):
       self.idCard=idCard
       self.name=name
       self.balance=balance

class ATM():
    def __init__(self,cardId,cardPasswd,cardBalance):
        self.cardId=cardId
        self.cardPasswd=cardPasswd
        self.cardBalance=cardBalance

    #随机生成六位数账号
    def ranmodcardId(self):
            stu=""
            stu="".join(str(i) for i in random.sample(range(0,9),6))
            BankCard.idCard=stu
            print(BankCard.idCard)

    #查询余额
    def chackBalance(self):
        self.cardId=input("请输入您的卡号:")
        if self.cardId==BankCard.idCard:
            print("查询成功！余额为{}".format(BankCard.balance))
        else:
            print("查询失败！")

    #存钱
    def saveMone(self):
        self.cardId = input("请输入您的卡号:")
        if self.cardId == BankCard.self.idCard:
            print("查询成功！")
        getNum=int(input("请输入存款金额："))
        if getNum<0:
            print("输入有误，请重新输入！")
        else:
            BankCard.balance+=getNum
            print("您的余额为{}".format(BankCard.balance))

    #取钱
    def getMoney(self):
        self.cardId = input("请输入您的卡号:")
        if self.cardId == BankCard.idCard:
            print("查询成功！")
        getNum = int(input("请输入存款金额："))
        if getNum < 0:
            print("输入有误，请重新输入！")
        else:
            BankCard.balance -= getNum
            print("您的余额为{}".format(BankCard.balance))

    #转账
    def transfer(self,transferNum,transMoney):
        self.cardId = input("请输入您的卡号:")
        transferNum=input("请输入对方卡号：")
        transMoney=input("请输入转账金额：")
        if transMoney>self.BankCard.balance:
            print("余额不足，转账失败！")
        else:
            BankCard.balance-=transMoney
            print("转账成功，系统将在3s后退出.....")
            time.sleep(3)



# 2.编写一个计数器，能够记录一个类创建了多少个对象。
class CountNum:
    count=0
    def __new__(cls, *args, **kwargs):
        cls.count+=1
    def __init__(self):
        CountNum.count+=1
    def target1(self):
        CountNum.count += 1
    def target2(self):
        CountNum.count += 1

# 3.编写程序，设计单张扑克牌类Card，具有花色，牌面与具体值。
# 同时设计整副扑克牌类Cards，具有52张牌。设计一个发牌的函数，
# 对任意三张牌断定牌的类型。
# 类型包括：
# 三条：三张牌value一样
# 一对：两张value一样
# 顺子：三张牌挨着
# 同花：三张牌type一样
# 同花顺：挨着，类型一样
# 其余都是散牌

import random
class card:
    def __init__(self,cards):
       self.cards=cards

    def pokers(self):
        pokers=[]
        poker=[]
        for i in ['♥','♠','♦','♣']:
            for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                poker.append(i)
                poker.append(j)
                pokers.append(poker)
                poker=[]

    def sendPokers(self):
        # 获取手牌数字
        str_tool1 = '0123456789TJQKA'
        num1 = [random.randint(2, 13) for _ in range(3)]
        poker_number = [str_tool1[x] for x in num1]
        # 获取手牌花色
        str_tool2 = '♥','♠','♦','♣'
        num2 = [random.randint(1, 4) for _ in range(3)]
        poker_suit = [str_tool2[x] for x in num2]
        # 生成手牌组合（列表）
        cards = [poker_number[x] + poker_suit[x] for x in range(3)]
