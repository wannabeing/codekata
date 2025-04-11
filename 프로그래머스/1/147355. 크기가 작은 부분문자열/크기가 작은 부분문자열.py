def solution(t, p):
    answer = 0
    
    n = len(p) # p의 길이
    number = int(p) # p를 정수형으로 변환
    
    for i in range(len(t) - n + 1):
        tmp = int(t[i:n+i]) # i부터 (p의길이)+i까지 자름
        if tmp <= number:
            answer += 1
    return answer