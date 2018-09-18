# random产生随机数模块
import random
# 1.返回一个0到1之间的浮点数，包括0不包括1  [0,1)
print(random.random())
# while random.random()!=0:
#     pass
# print("已经获得了")

# 2. randint(a,b)产生  a<=x<=b 包含起止点
print(random.randint(1,3))

# 3.包含start，不包含end
# random.randrange(start,stop,step)
print(random.randrange(1,10,2))

# 4.random.uniform(a,b) 可以产生 a<=x<=b  浮点数，闭区间
# print(random.uniform(2.3,2.5))

# 5. choice(seq),从迭代对象中随机选择一个元素
print(random.choice([1,3,5,6,7,8]))

# 6. choices(seq,权重,k)k是取几个值
print(random.choices([1,2,3,4,5],weights=[1,1,1,1,10000],k=3))

# 7.sample(seq,k) k是抽取的个数
# 跟choices不同在于取完元素之后，不放回
print(random.sample([1,2,3,4,5],k=3))

# 8.shuffle(seq) 可以对列表进行打乱顺序后重新输出列表
# 就地洗牌
li=[1,2,3,4,5]
random.shuffle(li)
print(li)


