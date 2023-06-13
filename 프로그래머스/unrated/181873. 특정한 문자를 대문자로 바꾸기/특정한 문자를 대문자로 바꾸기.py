def solution(my_string, alp):
    answer = ''
    if alp in my_string:
        for i in my_string:
            if i == alp:
                answer += i.upper()
            else:
                answer += i
    else:
        answer = my_string
                
    return answer