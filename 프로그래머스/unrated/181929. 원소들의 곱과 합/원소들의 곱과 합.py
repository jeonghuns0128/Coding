def solution(num_list):
    answer = 0
    add_total = 0
    multi_total = 1
    
    for i in num_list:
        multi_total *= i
        add_total += i
    
    if multi_total < add_total**2:
        answer = 1
    
    return answer