# 과일장수
def solution(k, m, score):
    answer = 0
    score =sorted(score,reverse=True)
    i = 0
    while (i + m <= len(score)):
        box = score[i : i + m]
        price = min(box) * len(box)
        answer += price 
        i += m        
    return answer



print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))

# 다른사람풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

solution = lambda _, m, s: sum(sorted(s)[-m::-m]) * m

# 삽질
"""
def solution(k,m,score):
    total = 0 
    score = sorted(score)[len(score)%m:]
    for i in range(0,len(score),m):
        if len(score) >= m:
            total += score[0] * m
            score = score[m:]
    return total
"""
