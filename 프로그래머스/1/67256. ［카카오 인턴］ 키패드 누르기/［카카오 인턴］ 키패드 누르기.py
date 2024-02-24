def solution(numbers, hand):
    answer = ''
    keypad = []
    lloc = (3,0)
    rloc = (3,2)
    for h in range(4):
        for w in range(3):
            keypad.append((h,w))
            
    for num in numbers:
        if num in [1,4,7]:
            lloc = keypad[num-1]
            answer += "L"
        elif num in [3,6,9]:
            rloc = keypad[num-1]
            answer += "R"               
        else:
            if num == 0:
                num = 11
            right = abs(rloc[0]-keypad[num-1][0]) + abs(rloc[1]-keypad[num-1][1])
            left = abs(lloc[0]-keypad[num-1][0]) + abs(lloc[1]-keypad[num-1][1])
            if right > left:
                lloc = keypad[num-1]
                answer += "L"
            elif right < left:
                rloc = keypad[num-1]
                answer += "R"
            else:
                if hand == "right":
                    rloc = keypad[num-1]
                    answer += "R"
                else:
                    lloc = keypad[num-1]
                    answer += "L"
    return answer