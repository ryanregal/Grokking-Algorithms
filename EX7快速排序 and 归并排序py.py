def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

def mergeSort(array):
    #归并排序
    if len(array)<2:
        return array
    else:
        mid=int(len(array)/2)#将列表分成更小的两个列表
        #分别对左右两个列表进行处理，分别返回两个排序好的列表
        left=mergeSort(array[:mid])
        right=mergeSort(array[mid:])
        return merge(left,right)

def merge(left,right):#并两个一已排序好的列表，产生一个新列表
    result=[]
    i=0
    j=0
    while i <len(left) and j <len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

#试验
print(quicksort([10,5,2,3]));

print(mergeSort([10,5,2,3]))
