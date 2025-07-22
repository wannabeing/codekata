def solution(sizes):
    maxW = 0
    maxH = 0
    for w, h in sizes:
        w, h = max(w, h), min(w, h)
        maxW = max(maxW, w)
        maxH = max(maxH, h)
    return maxW * maxH
