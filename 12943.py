# 콜라츠 추측
def solution(n):
    tmp = 0
    while n != 1:
        if tmp == 500: 
            return -1
        else:
            if n % 2 == 0:
                n = n/2
            else:
                n= n*3+1
            tmp += 1
    return tmp

print(solution(626331))

# 다른사람풀이
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1