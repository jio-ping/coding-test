# JadenCase문자열만들기
def solution(s):
    return (" ".join([ss.capitalize() for ss in s.split(" ")]))
        
print(solution("3people unFollowed me"))