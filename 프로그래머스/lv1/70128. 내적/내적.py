def solution(a, b):
    answer = 0
    if len(a) == len(b):
        for num,i in enumerate(a):
            answer += a[num]*b[num]
    return answer