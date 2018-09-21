# 1.r+，w+与a+都可以读取文件与写入文件，指出三者间的区别。
# with open("c:/a.txt","r+") as f :
#     f.write("hello")
# with open("c:/a.txt","w+") as f :
#     f.write("1")
with open("c:/a.txt","a+") as f :
    f.write("333")
# r+  可读可写，但是文件必须存在，直接覆盖写，不是删除了源文档后再写
# w+  可读可写，文件如果不存在，不会报错，如果文件已存在，删除源文档内容之后再重新写
# a+  可读可写，文件如果不存在，不会报错，如果文件已存在，追加写。


# 2.重命名文件：编写一个函数，接收一个路径，去掉路径下所有的文件（包括子目录的文件），
# 文件名末尾的特定字符串。
# def fun（路径，“广告”）
import  os
# os.walk()
# os.listdir()
# os.path.isdir()
#方式一：walk
def ren(path,del_content):
    ts=reversed(list(os.walk(path))) # 从文件夹的内侧往外遍历。
    # print(list(ts))
    # ts=os.walk(path)
    for i in ts:
        # print(i)
        for k in range(2,0,-1): # 将文件和子文件夹都改变，顺序先该文件，再改文件夹
            for j in i[k]:
                orgin_name=os.path.join(i[0],j)
                new_name=os.path.join(i[0],j.replace(del_content,""))
                os.rename(orgin_name,new_name)
        # for j in i[0]:
        #     orgin_name = os.path.join(i[0], j)
        #     new_name = os.path.join(i[0], j.replace(del_content, ""))
        #     os.rename(orgin_name, new_name)
        # for j in i[1]:
        #     orgin_name=os.path.join(i[0],j)
        #     new_name=os.path.join(i[0],j.replace(del_content,""))
        #     os.rename(orgin_name,new_name)


ren("C:/abc","广告")
# 方式二：
# os.listdir()
# os.path.isdir()
def ren2(path,del_content):
    files=os.listdir(path)
    print(files)
    for f in files:
        orgin_name=os.path.join(path,f)
        new_name=os.path.join(path,f.replace(del_content,""))
        os.rename(orgin_name,new_name)

        if os.path.isdir(new_name):
            ren2(new_name,del_content)
# ren2("c:/abc","广告")


#
# 3.获取文本文件中最长一行的长度。（一条语句）
print(max([len(line) for line in open("c:/a.txt")]))

# 4.对两个文件进行合并\文件的复制。
# with open("c:/a.txt") as f1,open("c:/b.txt") as f2,open("c:/c.txt","at") as f3:
#     for line in f1:
#         f3.write(line)
#     for line in f2:
#         f3.write(line)




# 5.查找文件夹中所有文件，只要包含Happy，New ，Year，任何一个词，的文件就输出文件的名字
ts=os.walk("c:/abc")
keyswords=["Happy","New","Year"]
for roots,dirs,files in ts:
    # print(i)
    # print(roots,dirs,files)
    #  为了可以open打开文件读取，路径进行合并
    for fn in files:
        fpath=os.path.join(roots,fn)
        with open(fpath) as f:
            fstr=f.read()
            for k in keyswords:
                if k in fstr:
                    print("{}路径中存在{}".format(fpath,k))
                    break





# 6.对文件进行简单加密。（bytes(iterable)构造器）加密方式为文件的每个字符的字节+1
# 加密：就编码格式修改
# 对字符串的加密，字符串变成字节，字节存的整数
# def encrpt(oldpath,newpath):
#     with open (oldpath,"rb") as f1,open(newpath,"wb") as f2:
#         for line in f1:
#             print(line)
#             for v in line:
#                 f2.write(bytes([v+1])) # bytes函数的功能，参数是迭代对象，可以将参数变成ascii码，再对其进行处理，再转回bytes
#                 # chr(ord(v)+1)
#
# encrpt("c:/a.txt","c:/a_new.txt")
# def de_encrpt(oldpath,newpath):
#     with open(oldpath, "rb") as f1, open(newpath, "wb") as f2:
#         for line in f1:
#             print(line)
#             for v in line:
#                 f2.write(bytes([v - 1]))  # bytes函数的功能，参数是迭代对象，可以将参数变成ascii码，再对其进行处理，再转回bytes
#                 # chr(ord(v)+1)
# de_encrpt("c:/a_new.txt","c:/a_new_new.txt")