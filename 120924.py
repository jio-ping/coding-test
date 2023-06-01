"""다음에 올 숫자"""

def solution(common):
    if common[1] - common[0] == common[2]-common[1]:
        a = common[1]-common[0]
        return a+common[-1]
    elif common[1]/ common[0] == common[2]/common[1]:
        a = common[1]/common[0]
        return int(a*common[-1])

print(solution([2, 4, 8]))


# 다른사람풀이
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer