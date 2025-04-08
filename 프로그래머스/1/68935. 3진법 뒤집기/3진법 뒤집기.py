def solution(n):
    answer = 0
    three = ""
    while n > 0:
        three = str(n % 3) + three # 나머지 + three
        n = n // 3 # 몫을 n에 저장
    reverseThree = ''.join(reversed(three))
    return int(reverseThree, 3)