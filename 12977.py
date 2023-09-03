# 소수만들기
from itertools import combinations
def solution(nums):
    cnt = 0
    for comb in combinations(nums,3):
        if isPrime(sum(comb)):
            cnt += 1
    return cnt
def isPrime(n):
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

print(solution([1,2,3,4]))