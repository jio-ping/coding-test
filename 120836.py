"""순서쌍의 개수"""
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i ==0 :
            answer. append(i)
    return len(answer)

print(solution(100))

# 다른사람풀이

def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))