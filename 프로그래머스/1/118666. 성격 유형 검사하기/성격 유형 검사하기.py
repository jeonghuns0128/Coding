def solution(survey, choices):
    answer = ''
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    
    for i, choice in enumerate(choices):
        if choice == 1:
            dic[survey[i][0]] += 3
        elif choice == 2:
            dic[survey[i][0]] += 2
        elif choice == 3:
            dic[survey[i][0]] += 1
        elif choice == 5:
            dic[survey[i][1]] += 1
        elif choice == 6:
            dic[survey[i][1]] += 2
        elif choice == 7:
            dic[survey[i][1]] += 3
    print(dic)
    indicators = ["RT", "CF", "JM", "AN"]
    
    for i in range(0,4):
        if(dic[indicators[i][0]] >= dic[indicators[i][1]]):
            answer += indicators[i][0]
        else:
            answer += indicators[i][1]
        print(answer)
    
    
    return answer