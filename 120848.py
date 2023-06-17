def solution(n):
    tmp = 1
    for i in range(1,10):
        tmp *= i
        if tmp > n:
            return i-1
        elif tmp == n :
            return i
    return n
print(solution(7))

