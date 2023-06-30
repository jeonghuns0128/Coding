def solution(num_list):
    answer = []
    last_index = len(num_list) - 1
    if num_list[last_index-1] < num_list[last_index]:
        num_list.append(num_list[last_index] - num_list[last_index-1])
    else:
        num_list.append(num_list[last_index]*2)
    answer = num_list
    return answer