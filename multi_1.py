from multiprocessing import Process
from time import ctime,sleep

a = 1
def func():
    sleep(2)
    global a
    a = 10000
    print("子进程中访问a",a)
    print(ctime())

p = Process(target=func)
# 启动子进程，func函数自动调用

p.start()
sleep(3)
print("父进程中的a",a)
# 阻塞等待回收子进程
p.join()


