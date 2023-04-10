def solution(M, N):
    answer = 0
    
    if M > 0 and N > 0:
        answer = (M-1)+(M*(N-1))
    return answer