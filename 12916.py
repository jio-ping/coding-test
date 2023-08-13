# 문자열 내  p와 y의 개수
def solution(s):
    s = s.upper()
    return s.count("P")==s.count("Y") 
print(solution("pPoooyY"))