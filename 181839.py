# 주사위게임 1
def is_odd(n):
    if n%2 !=0:
        return True
def solution(a,b):
    if is_odd(a) and is_odd(b):
        return a**2 + b**2
    elif is_odd(a) or is_odd(b):
        return 2*(a+b)
    else:
        return abs(a-b)