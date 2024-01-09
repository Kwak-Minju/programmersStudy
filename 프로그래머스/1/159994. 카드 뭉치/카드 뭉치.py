def solution(cards1, cards2, goal):
    answer = ''
    a = 0
    b = 0
    
    for i in goal:
        print("goal-",i)
        print("a", a ,"<", len(cards1))
        print("b", b ,"<", len(cards2))
        if(a < len(cards1) and b < len(cards2)):
            print("===")
            if(cards1[a] == i):
                print("cards1[a]",cards1[a])
                a +=  1
                if(a >= len(cards1)):
                    a -=  1
            
            elif(cards2[b] == i):
                print("cards2[b]",cards2[b])
                b +=  1
                if(b >= len(cards2)):
                    b -=  1
            else:
                return "No"
    print("a=",a,"/b=",b)
    return "Yes"
    # if(a == (len(cards1)-1) and b == (len(cards2)-1)):
    #     return "Yes"
    # else:
    #     return "No"