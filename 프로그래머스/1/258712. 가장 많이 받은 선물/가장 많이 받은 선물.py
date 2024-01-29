def solution(friends, gifts):
    answer = 0
    # 주고 받은 선물 현황
    info = {}
    
    for f in friends:
        infos = {}
        for fs in friends:
            if f != fs:
                infos[fs]=0         
        info[f] = infos
        
    for i in gifts:
        a= i.split()
        info[a[0]][a[1]] += 1
    
    nextMonthGift = {}
    
    for i in friends:
        nextMonthGift[i] = 0
    
    for i in range(0,len(friends)-1):
        for f in range(i+1,len(friends)):
            if info[friends[i]][friends[f]] > info[friends[f]][friends[i]]:
                nextMonthGift[friends[i]] += 1
            elif info[friends[i]][friends[f]] < info[friends[f]][friends[i]]:
                nextMonthGift[friends[f]] += 1
            else:
                send = {friends[i] : 0, friends[f] : 0}
                rec = {friends[i] : 0 , friends[f] : 0}
                # for a in info[friends[i]]:
                send[friends[i]] = sum(info[friends[i]].values())
                send[friends[f]] = sum(info[friends[f]].values())
                for j in friends:
                    if j != friends[i]:
                        rec[friends[i]] += info[j][friends[i]]
                    if j != friends[f]:
                        rec[friends[f]] += info[j][friends[f]]
                if (send[friends[i]]-rec[friends[i]]) > (send[friends[f]]-rec[friends[f]]):
                    nextMonthGift[friends[i]] += 1
                elif (send[friends[i]]-rec[friends[i]]) < (send[friends[f]]-rec[friends[f]]):
                    nextMonthGift[friends[f]] += 1
    allValue = nextMonthGift.values()
    maxValue = max(allValue)
    
    return maxValue