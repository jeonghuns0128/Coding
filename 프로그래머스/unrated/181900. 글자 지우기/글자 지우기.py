def solution(my_string, indices):
    answer = ''
    for num,i in enumerate(my_string):
        if num not in indices:
            answer += i
    return answer