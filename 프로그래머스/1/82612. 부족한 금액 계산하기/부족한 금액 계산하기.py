def solution(price, money, count):
    fee = 0
    for c in range(count+1):
        fee += c * price
    if money > fee :
        return 0
    return fee-money