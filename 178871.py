# 달리기경주
def solution(players,callings):
    players_score = {player:i for i, player in enumerate(players)}
    for calling in callings:
        calling_index = players_score[calling]
        players_score[calling] -= 1
        players_score[players[calling_index-1]] +=1
        players[calling_index-1], players[calling_index] = players[calling_index], players[calling_index-1]
    return players
        


print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])) 


# 시간초과
"""
def solution(players,callings):
    for calling in callings:
        calling_index = players.index(calling)
        players[calling_index] = players[calling_index-1]
        players[calling_index-1]=calling
    return players
"""

# 다른사람풀이

def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players