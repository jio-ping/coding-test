# 내적
def solution(a,b):
    return sum([a[i]*b[i] for i in range(len(a))])

# print(solution([1,2,3,4],[-3,-1,0,2]))

# 다른사람풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

solution = lambda x, y: sum(a*b for a, b in zip(x, y))
