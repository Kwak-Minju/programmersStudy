def solution(n, lost, reserve):
    
    gu = list(set(lost)&set(reserve))
    
    if len(gu) > 0 :
        for g in gu:
            reserve.remove(g)
            lost.remove(g)
            
    for l in sorted(lost):
        if l-1 in reserve:
            # answer += 1
            reserve.remove(l-1)
        elif l+1 in reserve:
            # answer+= 1
            reserve.remove(l+1)
        else:
            n -=1
    return n