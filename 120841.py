"""점의 위치 구하기"""
def solution(dot):
    if dot[0]>0:
        if dot[1]>0:
            return 1
        else:
            return 4
    else:
        if dot[1]>0:
            return 2
        else:
            return 3
        
print(solution([2,4]))

# 다른사람풀이
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

def solution(dot):
    a, b = 1, 0
    if dot[0]*dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2*a-b