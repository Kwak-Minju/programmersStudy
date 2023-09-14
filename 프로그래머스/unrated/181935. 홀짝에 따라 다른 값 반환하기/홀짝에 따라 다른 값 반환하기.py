def solution(n):    
    answer = 0
    
    if n % 2 ==0:
        chk = 0
        while chk <= n:
            answer += chk**2
            chk+=2
    else:
        chk = 1
        while chk <= n:
            answer += chk
            chk+=2
    return answer