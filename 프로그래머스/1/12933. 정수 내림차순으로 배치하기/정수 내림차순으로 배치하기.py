def solution(n):
    answer = ''
    for i in sorted(list(str(n)),reverse = True):
        answer += i
    return int(answer)