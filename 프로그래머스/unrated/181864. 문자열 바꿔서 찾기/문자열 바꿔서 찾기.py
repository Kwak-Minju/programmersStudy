def solution(myString, pat):
    print(myString)
    c= myString.replace("A","X")
    print(c)
    k= c.replace("B","A")
    print(k)
    h= k.replace("X","B")
    print(h)
    return 1 if pat in h else 0