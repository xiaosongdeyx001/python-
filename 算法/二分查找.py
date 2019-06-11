#最多猜测的次数与列表长度一致的称为 线性时间
#时间复杂度为O(logN)
def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid=int((low+high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None
my_list=[1,3,4,5,7,9]
print(binary_search(my_list,4))
print(binary_search(my_list,6))

