def solution(lottos, win_nums):
    answer = []
    max_match = 0
    min_match = 0
    dic_rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1 }
    
    for lotto in lottos:
        if lotto == 0:
            max_match += 1
        else:
            if lotto in win_nums:
                max_match += 1
                min_match += 1
    
    answer.extend([dic_rank[max_match], dic_rank[min_match]])
    
    return answer