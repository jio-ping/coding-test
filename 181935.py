"""홀짝에 따라 다른 값 반환하기

n-홀수 =>n이하의 홀수 양의 정수합
n-짝수 => n이하의 짝수인 양의 정수의 제곱"""
def solution(n):
    count = 0
    for i in range (n,0,-2):
        if i % 2 == 0:
            count += i**2
        else:
            count += i
    return count

print(solution(7))


# 다른사람풀이 
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)


