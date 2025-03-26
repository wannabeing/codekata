def solution(phone_number):
    # *을 (번호길이-4)만큼 출력, 번호 뒷 4자리 합쳐서 출력
    return '*'*(len(phone_number) - 4) + phone_number[-4:]