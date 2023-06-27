def solution(myString):
    answer = []
    result = 0
    for num,i in enumerate(myString):
        if (num+1) != len(myString):
            if i == 'x':
                answer.append(result)
                result = 0
            else:
                result += 1
        else:
            if i == 'x':
                answer.append(result)
                answer.append(0)
            else:
                result += 1
                answer.append(result)
            
        
            
    return answer