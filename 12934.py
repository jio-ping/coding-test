# 정수제곱근판별
import math
def solution(n):
    answer = 0
    num = n ** 0.5

    if num == int(num):
        return (num+1) ** 2
    else:
        return -1

print(solution(17))