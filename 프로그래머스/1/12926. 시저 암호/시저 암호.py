def solution(s, n):
    answer = ''
    for sc in s:
        if sc.isupper():
            if ord(sc) + n > 90:
                answer += chr(ord(sc) + n -26)
            else:
                answer += chr(ord(sc) + n)
        elif sc.islower():
            if ord(sc) + n > 122:
                answer += chr(ord(sc) + n -26)
            else:
                answer += chr(ord(sc) + n)
        else:
            answer += sc
    return answer