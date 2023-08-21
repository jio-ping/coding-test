# 크기가 작은 부분 문자열
def solution(t,p):
    cnt = 0 
    while len(t)>0:
        if t[:len(p)]<=p and len(t[:len(p)])==len(p) :
            cnt += 1
        t = t[1:]
    return cnt
print(solution("3141592","271"))

# 다른사람풀이
def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer