def findSmallest(arr):
    smallest = arr[0]   #存储最小的值
    smallest_index = 0  #存储最小的索引
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#排序算法
def selectionSort(arr):  #对数组进行排序
    newArr = []
    for i in range(len(arr)):# 找出数组中最小的元素，并将其加到新的数组中
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return  newArr
print (selectionSort([1,6,8,9,4]))
