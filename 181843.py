# 부분문자열인지 확인하기
def solution(my_string, target):
    return 1 if target in my_string else 0

# 다른사람풀이
def solution(my_string, target):
    return int(target in my_string)
