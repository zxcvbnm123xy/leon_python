import os
import os.path
# 1.r+，w+与a+都可以读取文件与写入文件，指出三者间的区别。
# r+: 读写，不是新创建写
# with open("d:/abc.txt","r+") as f1:
#     print(f1.read())

# a+:读写，追加写，如果文件不存在会创建
# with open("d:/abc.txt","a+") as f2:
#     # print(f2.read())
#     f2.write("bbbbbb")

#w+：读写，覆盖写，如果文件不存在会创建
# with open("d:/abc.txt", "w+") as f3:
#     # print(f3.read())
#     f3.write("cccccccc")

# 2.重命名文件：编写一个函数，接收一个路径，去掉路径下所有的文件（包括子目录的文件），文件名末尾的特定字符串。
# def fun（路径，“广告”）
# def rename(path,del_content):
#     files=os.listdir(path)
#     for f in files:
#         orgin_name=os.path.join(path,f)
#         new_name=os.path.join(path,f.replace(del_content,""))
#         # print(orgin_name)
#         # print(new_name)
#         os.rename(orgin_name,new_name)
#         if os.path.isdir(new_name):
#             rename(new_name,del_content)
# rename("d:/abc","广告")
#
# 3.获取文本文件中最长一行的长度。（一条语句）
# with open("d:/abc.txt","") as f:
#     longestLine=max(len(line.strip() for line in f))
# longest=0
# longline=""
# with open("d:/abc.txt","") as f:
#     for line in f:
#         linelen=len(line)
#         if linelen>longest:
#             longest=linelen
#             longline=line
# print("longest line".format(longline))
# print("The number of lingest line".format(longest))

# print(max([len(i.strip("\n")) for i in open("d:/abc.txt")]))

# 4.对两个文件进行合并\文件的复制。
# with open("d:/abc/t1.txt") as f1,open("d:/abc/t2.txt") as f2,open("d:/abc/t3.txt","a+") as f3:
#     for line in f:
#         f3.write(line)
#     for line in f2:
#         f3.write(line)
# with open("d:/abc/t3.txt") as f:
#     print(f.read())

# 复制
# with open("d:/abc/t1.txt") as f,open("d:/abc/t4.txt","wt") as f4:
#     for line in f:
#         f4.write(line)
# with open("d:/abc/t4.txt") as f:
#     print(f.read())

# 5.查找文件夹中所有文件，只要包含Happy，New ，Year，任何一个词，
#的文件就输出文件的名字
keyswords=["Happy","New","Year"]
p=os.walk("d:/abc")
for roots,dirs,files in p:
    for fn in files:
        fnabs_path=os.path.join(roots,fn)
        with open(fnabs_path) as fp:
            fp_str=fp.read()
            for k  in keyswords:
                if k in fp_str:
                    print("{}文件中包含{}".format(fnabs_path,k))



# 6.对文件进行简单加密。
# （bytes(iterable)构造器）加密方式为文件的每个字符的字节+1
def encrypt(path1,path2):
    with open(path1,"rb") as f,open(path2,"w+b") as f2:
        for line in f:
            for v in line:
                f2.write(bytes([v+1]))

def de_encrypt(path1,path2):
    with open(path1, "rb") as f, open(path2, "w+b") as f2:
        for line in f:
            for v in line:
                f2.write(bytes([v-1]))

encrypt("d:/abc.txt","d:/abc_new.txt")
de_encrypt("d:/abc_new.txt","d:/abc_new_new.txt")