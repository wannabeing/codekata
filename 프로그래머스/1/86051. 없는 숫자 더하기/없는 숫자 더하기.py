def solution(numbers):
    sum = 0
    
    # 0 ~ 9
    for i in range(10):
        # numbers 안에 i가 없으면 sum에 해당 값 더하기
        if i not in numbers:
            sum += i
    return sum
            
    