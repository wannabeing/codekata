def solution(k, score):
    명예의전당 = []
    발표점수 = []

    for s in score:
        명예의전당.append(s)
        명예의전당.sort(reverse=True)

        if len(명예의전당) > k:
            명예의전당 = 명예의전당[:k]

        발표점수.append(명예의전당[-1])

    return 발표점수