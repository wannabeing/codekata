def solution(x):
    answer = False
    sum = 0
    
    # 정수를 한자리씩 str로 받음
    for i in str(x):
        # 받은 값을 sum에 각각 저장
        sum += int(i)
    # 모든 자릿수의 합이 받은 정수로 나누어떨어지면 True
    if x%sum==0:
        answer=True
    
    return answer