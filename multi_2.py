from multiprocessing import Process
from time import ctime,sleep
import os

def eat():
    sleep(3)
    print("吃饭")
    print(os.getpid(),"的父进程",os.getppid())

def sle():
    sleep(1)
    print("睡觉")
    print(os.getpid(), "的父进程", os.getppid())

def dou():
    sleep(2)
    print("打豆豆")
    print(os.getpid(), "的父进程", os.getppid())


# 创建三个子进程
things = [eat,sle,dou]
pp = []  # 子进程对象
for th in things:
    p = Process(target=th)
    p.start()
    pp.append(p)

for i in pp:
    i.join()

print("这里是父进程",os.getpid())



