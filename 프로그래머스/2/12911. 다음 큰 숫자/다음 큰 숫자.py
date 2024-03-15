def solution(n):
    answer = 0
    
    oneNum = (bin(n)[2:]).count('1')
    
    while True:
        n += 1
        if oneNum == bin(n)[2:].count('1'):
            answer = n
            break
        
    
    return answer