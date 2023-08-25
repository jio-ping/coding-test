# 최솟값 만들기
def solution(A,B):
    total = 0 
    for pair in zip(sorted(A), sorted(B,reverse=True)):
        total += pair[0]*pair[1]
    return total

print(solution([1,2],[3,4]))