# 카드뭉치
def solution(cards1,cards2,goal):
    for goal_sentence in goal:
        if len(cards1)>0 and goal_sentence == cards1[0]:
            cards1= cards1[1:]
        elif len(cards2)>0 and goal_sentence == cards2[0] :
            cards2= cards2[1:]
        else:
            return "No"
    return "Yes"

print(solution( ["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))