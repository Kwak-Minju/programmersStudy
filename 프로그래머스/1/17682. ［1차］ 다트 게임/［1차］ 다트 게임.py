def solution(dartResult):
    answer = 0
    jump = []
    s =''
    for score in dartResult:
        if score.isalpha() == False:
            if score == "*":
                jump[-1] = jump[-1]*2
                if len(jump) >1:
                    jump[-2] = jump[-2]*2
            elif score == "#":
                jump[-1] = -jump[-1]
            else:
                s += score
        else:
            jump.append(int(s))
            s = ''
            if score == "S":
                pass
            elif score == "D":
                jump[-1] = jump[-1] ** 2
            elif score == "T":
                jump[-1] = jump[-1] ** 3
    return sum(jump)