"""짝수는 싫어요"""
def solution(n):
    return [i for i in range(n+1) if i %2 !=0]

print(solution(15))