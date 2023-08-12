# 나머지가 1이 되는 수 찾기
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]
print(solution(10))

