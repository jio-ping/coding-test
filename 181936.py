"""공배수"""
def solution(number, n, m):
    if number % n ==0 and number % m ==0:
        return 1
    else:
        return 0

print(solution(60,7,3))

# 다른사람풀이 

def solution(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))

def solution(number, n, m):
    return 1 if number%n==0 and number%m==0 else 0