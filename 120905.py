"""n의 배수 고르기"""
def solution(n,numlist):
    return [num for num in numlist if num%n==0]

print(solution(3,[4,54,6,7,3,9,10]))