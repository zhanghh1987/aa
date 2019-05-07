from multiprocessing import Process
import os
from time import sleep

# 复制上半部分
filename = "1.jpg"
n = os.path.getsize(filename)
n = n // 2
fr = open(filename,'rb')
def up():
    sleep(2)
    global n
    # 获取文件总字节数
    # fr = open(filename,'rb')
    fw = open("up.jpg", 'wb')
    while True:
        if n <= 1024:
            c = fr.read(n)
            fw.write(c)
            break
        c = fr.read(1024)
        fw.write(c)
        n -= 1024
    fw.close()
    fr.close()

# 复制下半部分
def down():
    # fr = open(filename,'rb')
    fw = open("down.jpg",'wb')
    # 文件指针偏移到中间位置
    fr.seek(n,0)
    while True:
        c = fr.read(1024)
        if not c:
            break
        fw.write(c)
    fw.close()
    fr.close()

# 创建两个子进程
p1 = Process(target=up)
p2 = Process(target=down)
#启动子进程
p1.start()
p2.start()
# 主进程阻塞等待回收两个子进程
p1.join()
p2.join()