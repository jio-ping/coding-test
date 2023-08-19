# 문자열다루기
def solution(string):
    return (len(string)== 4 or len(string)== 6) and string.isdigit()

print(solution("1a33"))

# 다른사람풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]