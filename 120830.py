"""양꼬치"""
def solution(n,k):
    return n*12000 + k *2000 - n//10 *2000

print(solution(64,6))
