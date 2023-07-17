def solution(common):
    answer = 0
    n = 0
    if common[1] - common[0] == common[2] - common[1]:
        n = common[1] - common[0]
        answer = common[len(common)-1] + n
    else:
        n = common[1] / common[0]
        answer = common[len(common)-1] * n
    return answer