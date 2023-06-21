def solution(myString):
    answer = ''
    for i in myString:
        if i < 'l':
            myString = myString.replace(i,'l')
    answer = myString
    return answer