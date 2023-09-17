def solution(str_list, ex):
    answer = ''
    for i in range(len(str_list)):
        if str_list[i].find(ex) == -1:
            answer += str_list[i]
    return answer