def solution(picture, k):
    answer = []
    for pic in picture:
        k_x_pickcell = ''
        for num,i in enumerate(pic):
            k_x_pickcell += i*k
            if len(pic) - 1 ==  num:
                for idx in range(k):
                    answer.append(k_x_pickcell)
    return answer