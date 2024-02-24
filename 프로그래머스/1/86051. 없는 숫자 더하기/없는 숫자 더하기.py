def solution(numbers):
    answer = 0
    for num in range(10):
        if numbers.count(num) == 0:
            answer += num        
    return answer