def solution(num, k):
    answer = 0
    char_num = str(num)
    if str(k) in char_num:
        for num,i in enumerate(char_num):
            if i == str(k):
                answer = num+1
                break
    else:
        answer = -1
    return answer