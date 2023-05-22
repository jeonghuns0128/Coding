def solution(nums):
    answer = 0
    nums_set = {}
    max_num = len(nums)/2
    
    nums_set = set(nums)
    if len(nums_set) >= max_num:
        answer = max_num
    else:
        answer = len(nums_set)
    
    
    return answer