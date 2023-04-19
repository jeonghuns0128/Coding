def solution(array):
    answer = 0
    array_string = ''.join(str(s) for s in array)
    answer = array_string.count('7')    
    return answer