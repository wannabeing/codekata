def solution(n):
    arr = list(str(n))
    arr.sort(reverse=True)
    
    result = int(''.join(arr))
    return result;