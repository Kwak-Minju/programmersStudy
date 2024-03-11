def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    l = {name:[] for name in id_list}
    res = {name:0 for name in id_list}
    ans=[]
    
    for re in report:
        r= re.split(" ")
        l[r[0]].append(r[1])
        
    for val in l.values():
        val = list(set(val))
        for v in val:
            res[v]+=1
            
    for resk in res:
        if res[resk] >= k:
            for i in range(len(id_list)):
                if resk in l[id_list[i]]:
                    answer[i] += 1

    return answer