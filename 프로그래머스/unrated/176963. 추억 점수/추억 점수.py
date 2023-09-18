def solution(name, yearning, photo):
    answer=[]
    hap = dict(zip(name,yearning))
    
    for per in photo:
        total=0
        for n in per:
            if n in name:
                total += hap[n]
        answer.append(total)
    return answer