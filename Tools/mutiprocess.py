import time
import multiprocessing


def hello(num):
    i = 0
    while i < num:
        i += 1
    print(i)


# if __name__ == '__main__':
#     ts = time.time()
#     hello(20000000)  # 第一次计算
#     hello(20000000)  # 第二次计算
#     hello(20000000)  # 第三次计算
#     te = time.time()
#     print("using time: " + str(te - ts) + "s")

# 20000000
# 20000000
# 20000000
# using time: 3.196721076965332s

if __name__ == '__main__':
    ts = time.time()
    j = 3
    while j >= 1:
        p = multiprocessing.Process(target=hello, args=(20000000, ))
        p.start()  # 启动进程
        j -= 1
    p.join()
    te = time.time()
    print("using time: " + str(te - ts) + "s")

# 20000000
# 20000000
# using time: 1.1055631637573242s
# 20000000

'''
if __name__ == '__main__' 如何正确理解?

一个python的文件有两种使用的方法，第一是直接作为脚本执行，第二是import到其他的python脚本中被调用（模块重用）执行。

因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，

在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，

而import到其他脚本中是不会被执行的。
'''
