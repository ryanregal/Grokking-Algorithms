#创建一个列表，包含要覆盖的州
states_needed=set(["mt","wa","or","id","nv","ut","ca","az"])

#创建散列表，表示广播台覆盖的州
stations={}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#使用集合来储存最终选择的广播站
final_stations=set()


while states_needed:#必须要有一个while循环！！！！
    best_station=None
    states_covered=set()#表示广播台覆盖的所有未覆盖州

    for station,states_for_station in stations.items():#遍历所有广播台，从中选择覆盖最多未覆盖州的广播台
        covered=states_needed & states_for_station
        if len(covered)>len(states_covered):
            best_station=station
            states_covered=covered
    final_stations.add(best_station)
    states_needed-=states_covered



print(final_stations)
