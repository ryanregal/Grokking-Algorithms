graph = {}#创建节点表
#a,b是start的邻居，数字储存它们的权重
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 6
     
graph["a"] = {}
graph["a"]["fin"] = 1
 
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
 
graph["fin"] = {}#终点没有任何邻居
 

 
infinity = float("inf")#创建开销表
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
 
parents={}#储存父节点
parents["a"]="start"
parents["b"] = "start"
parents["fin"] = None

processed=[]


def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    
    for node in costs:#遍历所有节点
        cost=costs[node]
        if cost<lowest_cost and node not in processed:#未被处理过
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node


node=find_lowest_cost_node(costs)#在未处理的节点中找出开销最小的节点
while node is not None:#循环直到node为none
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)#设该节点被标记过
    node=find_lowest_cost_node(costs)#找出接下来要找的节点


print(costs)
print(parents)
