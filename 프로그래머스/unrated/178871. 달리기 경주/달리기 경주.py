def solution(players, callings):
    # 1차 풀이
    # answer = []
    # for calling in callings:
    #     num = players.index(calling)
    #     pre_player = players[num-1]
    #     players[num-1] = calling
    #     players[num] = pre_player
    # answer = players
    
    rankDic = {}
    playerDic = {}
    answer = []
    
    for idx,player in enumerate(players):
        rankDic[player] = idx+1
        playerDic[idx+1] = player
    
    for calling in callings:
        calling_rank = rankDic[calling]
        pre_player = playerDic[calling_rank-1]
        
        rankDic[calling] = calling_rank-1
        rankDic[pre_player] = calling_rank
        
        playerDic[calling_rank-1] = calling
        playerDic[calling_rank] = pre_player
        
    answer = list(playerDic.values())
    
    return answer