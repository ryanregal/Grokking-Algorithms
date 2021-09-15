from collections import deque

def search(name):
    search_queue=deque()#一个队列
    search_queue+=graph[name]
    searched=[]
    while search_queue:#当队列不为空
        person=search_queue.popleft()#同时将搜索过的人清除
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a mango seller!")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1]=="m"


if __name__=='__main__':
    graph = {}#创建一个字典（散列表）储存元素
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"  ]
    graph["anuj"] = []
    graph["peggy"] = [] 
    graph["thom"] = []
    graph["jonny"] = []


search("you")

