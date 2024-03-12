def solution(array, commands):
    answer = []
    for com in commands:
        narr = array[com[0]-1:com[1]]
        sarr=sorted(narr)
        answer.append(sarr[com[2]-1])
        
    return answer