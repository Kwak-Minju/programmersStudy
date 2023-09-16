def solution(num_list, n):
    hap = []
    for i in range(0,len(num_list),n):
        hap.append(num_list[i])
    return hap