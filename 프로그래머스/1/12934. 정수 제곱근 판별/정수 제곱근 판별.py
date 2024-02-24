def solution(n):
    answer = 0
    ans = n ** (1/2)
    if int(ans) ** 2 == n:
        return (int(ans) +1)**2
    else:
        return -1