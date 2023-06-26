def solution(num_list):
    answer = -1
    for num,i in enumerate(num_list):
        if i < 0:
            answer = num
            break
    return answer