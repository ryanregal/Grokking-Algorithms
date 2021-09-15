def fact(x):#递归
    if x==1:
        return 1
    else:
        return x*fact(x-1)


def factorial(x,result): #尾递归
    if x == 1:
        return result
    else:
        return factorial(x-1,x*result)

print(fact(5))
print(factorial(5,1))
