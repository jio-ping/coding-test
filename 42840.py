# 모의고사..
# 수포자 is me.. 
"""
answer   : 1, 2, 3, 4, 5, 1, 2, 3, 4, 5

1번수포자 : 1, 2, 3, 4, 5
2번수포자 : 2, 1, 2, 3, 2, 4, 2, 5
3번수포자 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
"""
def solution(answer):
    first = [1, 2,3,4,5]
    second = [ 2, 1, 2, 3, 2, 4, 2, 5 ]
    third  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ]
    score =[0,0,0]
    for i in range(len(answer)):
        if answer[i]  == first[i%5]:
            score [0] += 1
        if answer[i]  == second[i%8]:
            score [1] += 1
        if answer[i] == third[i%10]:
            score[2] += 1
    if score.count(max(score)) > 2:
        answer= [] 
        for i in range(len(score)):
            if max(score) == score[i]:
                answer.append(i+1)
        return answer
    else:
        return [score.index(max(score))+1]

print(solution([1,3,2,4,2]))
