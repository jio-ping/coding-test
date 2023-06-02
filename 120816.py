"""피자나눠먹기(3)"""
import math
def solution(slice,n):
    return math.ceil(n/slice)

print(solution(1,1))

# 다른사람풀이
def solution(slice, n):
    return ((n - 1) // slice) + 1