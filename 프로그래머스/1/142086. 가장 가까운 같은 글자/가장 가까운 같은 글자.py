def solution(s):
    result = []
    arrs = {}
    
    for index, char in enumerate(s):
        if char in arrs:
            result.append(index - arrs[char])
        else:
            result.append(-1)
        arrs[char] = index
    return result