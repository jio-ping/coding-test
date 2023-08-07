# 유한소수 판별하기
def solution(a,b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            gcd = i 
            b //= gcd
            while b%2==0:
                b//=2
            while b%5==0:
                b//=5
            return 1 if b==1 else 2
print(solution(11,22))