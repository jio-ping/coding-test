"""피자나눠먹기(2)"""
import math
def solution(n):
    return (n*6//math.gcd(n,6)//6)

print(solution(4))

# 다른사람풀이 
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1

