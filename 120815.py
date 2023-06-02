"""피자 나눠 먹기 (2)"""
import math
def solution(n):
    return math.ceil((math.gcd(n,6)*(n+6))/6)

print(solution(4))