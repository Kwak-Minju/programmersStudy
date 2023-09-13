def solution(my_string, overwrite_string, s):  
    hap=''
    h=0
    chk= s+ len(overwrite_string)
    for i in range(len(my_string)):
        if i < s:
            hap += my_string[i]
        elif i >= s and i < chk:
            hap += overwrite_string[h]
            h+=1
        else:
            hap += my_string[i]
        i +=1
    return hap