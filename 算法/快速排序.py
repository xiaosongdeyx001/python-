def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]#有所有小于和等于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]#有所有大于基准值的元素组成的子数组
        return  quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10,5,2,3]))