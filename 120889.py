"""삼각형의 완성조건(1)"""
def solution(sides):
    sides=sorted(sides)
    if sides[0]+ sides[1]>sides[-1]:
        return 1
    else:
        return 2
    
print(solution([3,6,2]))

# 다른사람풀이

def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2