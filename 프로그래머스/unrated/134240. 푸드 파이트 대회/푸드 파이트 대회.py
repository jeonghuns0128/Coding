def solution(food):
    answer = ''
    reverse_answer = ''
    for num,value in enumerate(food):
        if num == 0:
            pass
        else:
            answer += str(num)*(value // 2)
            if (num+1) == len(food):
                reverse_answer = answer[::-1]
                answer += '0' + reverse_answer
    
    return answer