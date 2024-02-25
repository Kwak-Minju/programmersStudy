def solution(arr1, arr2):
    answer = []
    ans = []
    for a in range(len(arr1)):
        for b in range(len(arr1[0])):
            ans.append(arr1[a][b]+arr2[a][b])
        answer.append(ans)
        ans = []
        
    return answer