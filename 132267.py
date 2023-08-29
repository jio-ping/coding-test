# 콜라문제
def solution(a,b,n):
    # a: 바꾸기 위해 필요한 병 b: 주는 콜라 수 n : 내가 갖고 있는 병
    bottle = n
    getCola = 0
    while bottle >= a:
        getCola += bottle//a *b
        bottle = bottle // a *b + bottle % a
    return getCola
print(solution(2,1,20))
