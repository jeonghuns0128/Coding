def solution(num_list, n):
    answer = []
    for num,i in enumerate(num_list):
        if num+1 >= n:
            answer.append(i)
    return answer