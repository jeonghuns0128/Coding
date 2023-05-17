def solution(absolutes, signs):
    answer = 0
    for num,absolute in enumerate(absolutes):
        if signs[num]:
            answer += absolute
        else:
            answer -= absolute
    return answer