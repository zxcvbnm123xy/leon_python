# 1.矩形与正方形两个类，求周长与面积。分别使用不继承与继承两种方式，并总结出继承的优势。
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        return (self.length+self.width)*2
    def area(self):
        return self.length*self.width
r=Rectangle(3,5)
print(r.perimeter(),r.area())


class Square:
    def __init__(self,length):
        self.length=length
    def perimeter(self):
        return self.length*4
    def area(self):
        return self.length**2
s=Square(4)
print(s.area(),s.perimeter())

class Square(Rectangle):
    # 方式一：
    # def __init__(self,length):
    #     self.length=length
    #     self.width=length
    # 方式二：
    def __init__(self, length):
        super().__init__(length,length)
s1=Square(4)
print(s1.perimeter(),s1.area())


#
# 2.编写一个分页显示类，初始化传入记录总数。
# 希望可以通过设置每页记录数和页码，可以显示当前页的信息。
# 其中每页记录数与页码使用property实现。
# 注意，如果页码设置不正确（如<1或者>最大页码），提示错误信息。
# 设计方法能够返回当前页显示的记录区间。
# Page(20)
# pagesize=5
# # 一共应该有4页
# currenPage=6
# show可以显示第三页的信息
# 这是第11-15条记录。。。。
class Page:
    def __init__(self,total):
        self.total=total
        self.__currentPage=1
        self.__pageSize=None
        self.max_page=None
    def set_currentPage(self,currentPage):
        # 问题：设置当前页，currentPage可能不合法，<1  >最大页数
        self.__currentPage=currentPage
        # 20  4-----5
        # 21  4-----5+1
        max_page=self.total//self.get_pageSize()
        if self.total%self.get_pageSize()!=0:
            max_page+=1
        self.max_page=max_page
        if currentPage<1  or currentPage>max_page:
            raise ValueError("页码设置错误")
        else:
            self.__currentPage=currentPage
    def show(self):
        print("共{}条记录，共{}页，每页是{}条记录".format(self.total,self.max_page,self.get_pageSize()))
        print("当前是第{}页".format(self.get_currentPage()))
        # 20  5-----4       3(11-15)   4(16-20)
        # 23  5-----4+1     3(11-15)   4(16-20)  5(21-23)
        start=(self.get_currentPage()-1)*self.get_pageSize()+1
        if self.get_currentPage()==self.max_page:
            end=self.total
        else:
            end=self.get_currentPage()*self.get_pageSize()
        for i in range(start,end+1):
            print("第{}条记录".format(i))

    def set_pageSize(self,pageSize):
        # 问题：pageSize  >0
        if pageSize>0:
            self.__pageSize=pageSize
        else:
            raise ValueError("每页记录数应>0")

    # def getCurrentPage
    def get_currentPage(self):
        return self.__currentPage
    def get_pageSize(self):
        return self.__pageSize
    currentPage=property(get_currentPage,set_currentPage)
    pageSize=property(get_pageSize,set_pageSize)
page=Page(23)
page.pageSize=5
page.currentPage=4
page.show()

#
# 3.编写电脑类，提供一个方法，能够与移动设备（U盘，MP3，移动硬盘）进行读写交互。
# 如果参数类型不是移动设备的类型，则打印错误信息。MP3除了读与写之外，
# 还额外具有一个播放音乐的功能。

class MoveStore:
    def __init__(self,name):
        self.name=name
    def read(self):
        print("正在读取信息.......")
    def write(self):
        print("正在写信息......")
class Udisk(MoveStore):
    pass
class Mp3(MoveStore):
    def play(self):
        print("正在播放音乐")
class MobileDisk(MoveStore):
    pass

class Computer:
    def connect(self,moveStore):
        if not isinstance(moveStore,MoveStore):
            raise ValueError("不是移动设备，不能连接。。。")
        else:
            print("{}正在连接...".format(moveStore.name))
            moveStore.read()
            moveStore.write()
            if isinstance(moveStore,Mp3):
                moveStore.play()
class A:
    pass
a=A()
udisk=Udisk("U盘")
mp3=Mp3("mp3")
mobiledisk=MobileDisk("移动硬盘")
# c=Computer()
# c.connect(udisk)
# c.connect(mp3)
# c.connect(mobiledisk)
# c.connect(a)


# class Computer：
#   def connect(self,moveStore):
#     moveStore.read()
#     moveStore.writer()
#     如果是MP3,还可以播放音乐
# c.connect(a)
# c.connect(u)
# c.connect(moveDisk)
# c.connect(mp3)
#
# 4.编写如下的继承结构，
# 类C继承（A，B），类D继承（B，A），类E继承（C，D）或者（D，C），会出现什么情况？
class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(B,A):
    pass
class E(C,D):
    pass
# class F(A,B):
#     pass
# 继承的时候要保证所有父类的继承顺序是一致的。