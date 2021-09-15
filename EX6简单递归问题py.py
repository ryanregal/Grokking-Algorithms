def sum(list):#sum函数
    if list==[]:
        return 0
    return list[0]+sum(list[1:])

def count(list):#计算列表包含的元素数
    if list==[]:
        return 0
    return 1+count(list[1:])

def max(list):#求最大
    if len(list)==2:
        return list[0] if list[0]>list[1] else list[1]
    sub_max=max(list[1:])
    return list[0] if list[0]>sub_max else sub_max

#三个试验

a=[1,2,3,4,5]
print(sum(a))
print(count(a))
print(max(a))
