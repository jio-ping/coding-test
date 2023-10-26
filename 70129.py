# 이진변환반복하기
"""
이진변환 재 정의 
1. s의 모든 0 제거
2. 0을 제거한 s의 길이를 2진변환 

"""

def solution(n):
    cnt = 0 
    delete_zero = 0
    while 1:
        if n != "1":
            delete_zero+= n.count("0")
            cnt += 1
            n = str(bin(len(n)-delete_zero))[2:]
        pass
    return [cnt, delete_zero]

print(solution("110010101001"))

def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]