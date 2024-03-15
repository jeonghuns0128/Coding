def solution(s):
    answer = True
    
    # while True:
    #     if '()' in s:
    #         s = s.replace('()','',1)
    #     else:
    #         if s == '':
    #             answer = True
    #         else:
    #             answer = False
    #         break
    
    stack = []
    
    for idx,i in enumerate(s):
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        answer = True
    else:
        answer = False
    
    return answer