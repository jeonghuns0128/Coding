def solution(k, m, score):
    answer = 0
    # boxCnt = len(score) // m
    # answer = m * boxCnt
    score.sort()
    score.reverse()
    cnt = m-1
    
    for i,value in enumerate(score):
        if i == cnt:
            cnt += m
            answer += m * value
    
    return answer