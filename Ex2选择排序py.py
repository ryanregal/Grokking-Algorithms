def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr=[5,3,6,2,10]
print(findSmallest(arr))
print(selectionSort(arr))
#选择一个最小的数值加在新列表中，再在之前除去最小数的列表挑选一个新的最小数值。
