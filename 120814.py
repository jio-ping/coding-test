"""피자 나눠먹기 (1)"""
import math
def solution(n):
    return math.ceil(n/7)
print(solution(23))

# 다른 사람 풀이 
def solution(n):
    return (n - 1) // 7 + 1