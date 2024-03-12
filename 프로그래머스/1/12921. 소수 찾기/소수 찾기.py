def solution(n):
    answer = set(x for x in range(2,n+1))
    for num in range(2, int(n ** 0.5) + 1):
        if num in answer:
            answer -= set(x for x in range(num*2, n+1, num))
    return len(answer)