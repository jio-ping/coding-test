# 두개뽑아서 더하기
from itertools import combinations, permutations

def solution(numbers):
    return list(combinations(numbers,2))

print(solution([2,1,3,4,1]))