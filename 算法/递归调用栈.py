def fact(x):
    if x==1:
        return  1
    else:
        return  x * fact(x-1)
#打印每个数中的简单数
def print_items(list):
    for item in list:
        print(item)
#打印每个数之前都休眠一秒
from time import sleep
def print_item2(list):
    for item in list:
        sleep(1)
        print(item)
