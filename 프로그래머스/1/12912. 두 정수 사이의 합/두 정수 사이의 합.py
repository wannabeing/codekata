def solution(a,b):
    sum = 0
    start = a
    end = b
    
    if(a>b):
        start = b
        end = a

    for i in range(start, end+1):
        sum += i
    return sum



def solution(a, b):
    sum = 0
    if(a>b):
        tmp = a
        a = b
        b = tmp

    for i in range(a, b+1):
        sum +=i
    return sum








