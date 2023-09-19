# 달리기경주
def solution(players,callings):
    for calling in callings:
        calling_index = players.index(calling)
        players[calling_index] = players[calling_index-1]
        players[calling_index-1]=calling
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])) 