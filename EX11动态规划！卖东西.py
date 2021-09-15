#题干的各个变量
goods=[[1500,1],[3000,4],[2000,3]]


#函数,goods见上，size为背包大小

def bag(goods,size):
    
    #定义一个数组储存空格子，列有size个，行有goods个，初始量均为0
    
    #package_size修补range从0开始的bug
    
    cell=[[0 for col in range(size)] for row in range(len(goods))]

    package_size=[i+1 for i in range(size)]

    for j in range(size):
        if(goods[0][1]<=package_size[j]):
            cell[0][j]=goods[0][0]


    for i in range(1,len(goods)):
        for j in range(size):
            if(package_size[j]>goods[i][1])and (goods[i][0]+cell[i-1][package_size[j]-1-goods[i][1]])>cell[i-1][j]:
                cell[i][j]=goods[i][0]+cell[i-1][package_size[j]-goods[i][1]-1]
            elif(package_size[j]-goods[i][1]==0)and (goods[i][0]>cell[i-1][j]):
                cell[i][j]=goods[i][0]
            else:
                cell[i][j]=cell[i-1][j]
    print(cell)

    return cell[len(goods)-1][size-1]


print(bag(goods,4)) 
