"""k의개수"""
def solution(i,j,k):
    answer = 0
    for i in range(i,j+1):
        if str(i).count(str(k)):
            answer += str(i).count(str(k))
    return answer
# 다른사람풀이 
def solution(i,j,k):
    return sum([str(i).count(str(k)) for i in range(i,j+1)])

print(solution(1,13,1))