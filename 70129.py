# 이진변환반복하기
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