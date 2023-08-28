# 삼총사
from itertools import combinations
def solution(number):
    cnt = 0
    a = list(combinations(number,3))
    for aa in a:
        if sum(aa) == 0:
            cnt += 1
    return cnt

print(solution([-2, 3, 0, 2, -5]))