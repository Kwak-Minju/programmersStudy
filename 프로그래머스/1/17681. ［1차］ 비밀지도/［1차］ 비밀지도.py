def solution(n, arr1, arr2):
    answer = []
    ans = ''
    for na in range(n):
        # 이진수로 변환하고 0으로 채우기
        narr1 = format(arr1[na], 'b').zfill(n)
        narr2 = format(arr2[na], 'b').zfill(n)
        for i in range(n):
            if narr1[i] == '1' or narr2[i] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
        ans = ''
    return answer