def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    for idx,i in enumerate(A):
        answer += A[idx] * B[idx]
    return answer