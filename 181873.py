# 특정한 문자를 대문자로 바꾸기
def solution(my_string,alp):
    return my_string.replace(alp,alp.upper()) if alp in my_string else my_string

print(solution("progr","p"))