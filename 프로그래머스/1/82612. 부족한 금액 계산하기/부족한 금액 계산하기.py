def solution(price, money, count):
    needMoney = 0
    
    for i in range(1, count+1):
        needMoney += price * i
    
    if(money > needMoney):
        return 0
    return abs(needMoney - money)