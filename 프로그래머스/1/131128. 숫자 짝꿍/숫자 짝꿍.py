def solution(X, Y):
    answer = ''
    xcnt = 0
    ycnt = 0
    
    for i in range(9,-1,-1):
        xcnt = X.count(str(i))
        ycnt = Y.count(str(i))
        if xcnt !=0 and ycnt != 0:
            if i == 0 and len(answer) == 0:
                return "0"
            else:
                answer += str(i) * xcnt if xcnt < ycnt else str(i) * ycnt
    if answer == '':
        return "-1"
    else:
        return answer