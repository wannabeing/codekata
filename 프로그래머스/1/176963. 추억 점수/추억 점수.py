def solution(names, yearning, photos):
    answer = []
    dic = {name: score for name, score in zip(names, yearning)}
    for photo in photos:
        tmp = 0
        for person in photo:
            tmp += dic.get(person, 0)
        answer.append(tmp)
        
    return answer