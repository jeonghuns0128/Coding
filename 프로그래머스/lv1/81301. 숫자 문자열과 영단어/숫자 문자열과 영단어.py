def solution(s):
    answer = 0
    answer_string = ''
    char_string = ''
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    for char in s:
        if char >= '0' and char <= '9':
            answer_string += char
        else:
            char_string += char
            if len(char_string) > 2 and char_string in dic:
                answer_string += dic[char_string]
                char_string = ''
    answer = int(answer_string)
    
    return answer