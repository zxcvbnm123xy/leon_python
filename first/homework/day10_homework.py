# 编写“计算机类”，属性包括CPU型号，内存大小，硬盘大小。行为包括介绍CPU型号，展示内存大小，
# 展示硬盘大小，综合介绍。
class Computer:
    def __init__(self,model,memory,disk):
        self.model=model
        self.memory=memory
        self.disk=disk

    def cpu_model(self):
        print("计算机的型号是：{}".format(self.model))

    def cpu_memory(self):
        print("计算机的内存是：{}".format(self.memory))

    def cpu_disk(self):
        print("计算机的硬盘大小是：{}".format(self.disk))

    def computer_introduce(self):
        print("计算机的型号是{}，内存是{}，硬盘大小是{}".format(self.model,self.memory,self.disk))

c=Computer("i7","8.00G","500G")
c.cpu_memory()
c.computer_introduce()
