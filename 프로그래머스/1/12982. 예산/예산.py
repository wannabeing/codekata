def solution(d, budget):
    answer = 0
    values = sorted(d)
    for val in values:
        if budget >= val:
            budget -= val
            answer += 1
    return answer