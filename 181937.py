"""n의 배수
num이 n의 배수면 1 return 
아니면 0 return """

def solution(num,n):
    if num% n == 0:
        return 1
    else:
        return 0

# 다른사람풀이 
def solution(num, n):
    return int(not(num % n))