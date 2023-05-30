def solution(names):
    answer = []
    for num,name in enumerate(names):
        if num%5 == 0:
            answer.append(name)
    return answer