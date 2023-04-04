def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i,value in enumerate(name):
        dic[value] = yearning[i]
    
    for one_photo in photo:
        result = 0
        for i in one_photo:
            if i in dic:
                result += dic.get(i)
        answer.append(result)
    
    return answer