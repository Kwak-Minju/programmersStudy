def solution(x):
    hap = 0
    for i in list(str(x)):
        hap += int(i)
    if x % hap == 0:
        return True
    else:
        return False