def solution(numbers, n):
    hap = 0
    for i in numbers:
        print(i)
        if hap <= n:
            hap += i
    return hap