# 삼각형의 완성조건(2)
def solution(sides):
    return len([i for i in range(max(sides)-min(sides)+1,min(sides)+max(sides))])

print(solution([3,6]))

# 다른사람풀이
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1