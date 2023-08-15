# 두 정수 사이의 합
def solution(a,b):
    return sum([i for i in range(min(a,b),max(a,b)+1)])

print(solution(3,3))

# 다른사람풀이
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2