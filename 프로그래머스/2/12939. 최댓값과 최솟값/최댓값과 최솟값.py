def solution(s):
    answer = ''
    s_list = s.split()
    temp_result = []
    
    for i in s_list:
        temp_result.append(int(i))
        
    answer = str(min(temp_result)) + ' ' + str(max(temp_result))
    
    return answer