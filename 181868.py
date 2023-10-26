# 공백으로 구분하기
def solution(my_string):
    return [str for str in my_string.split(" ") if str!=""]
print(solution("   i lovw ypppu"))