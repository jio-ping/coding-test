# 명예의 전당 (1)
def solution(k,scores):
    reward = []
    min_score = [] 
    for score in scores:
        reward.append(score)
        reward=sorted(reward,reverse=True)[:k]
        min_score.append(reward[-1])
    return min_score

print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))