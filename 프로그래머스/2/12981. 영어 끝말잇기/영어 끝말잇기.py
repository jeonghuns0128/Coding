def solution(n, words):
    answer = []
    
    finalAphabet = ''
    firstAphabet = ''
    gameCnt = 0
    userNum = 0
    answerWord = []
    
    for idx,word in enumerate(words):
        if idx == 0:
            pass
        else:
            firstAphabet = word[0]
            if (firstAphabet == finalAphabet) and (word not in answerWord) and (len(word) > 1):
                pass
            else:
                userNum = (idx % n) + 1
                gameCnt = (idx // n) + 1
                break
        
        finalAphabet = word[-1]        
        answerWord.append(word)    
        
    answer.append(userNum)        
    answer.append(gameCnt)        
    
    return answer