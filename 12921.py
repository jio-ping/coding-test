# 소수찾기

import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 

# 효율 0 시간초과 
# def isPrime(n):
#     for i in range(2,n):
#         if n % i ==0:
#             return False
#     return True

def solution(n):
    return len([i for i in range(2,n+1) if isPrime(i)])

print(solution(10))


# 다른사람풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)