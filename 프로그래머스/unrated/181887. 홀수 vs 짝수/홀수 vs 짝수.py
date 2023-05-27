def solution(num_list):
    answer = 0
    add_odd = 0
    add_even = 0
    
    for idx,num in enumerate(num_list):
        if idx % 2 == 0:
            add_odd += num
        else:
            add_even += num
    if add_odd >= add_even:
        answer = add_odd
    else:
        answer = add_even
        
    return answer