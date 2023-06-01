"""제곱수 판별하기"""

def solution(n):
    from math import sqrt
    arr = str(sqrt(n)).split(".")
    if arr[-1] == "0":
        return 1
    else:
        return 2

print(solution(144))

# 다른사람풀이
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
