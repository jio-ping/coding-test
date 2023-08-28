# 접두사인지확인하기
def solution(my_string,is_prefix):
    return 1 if my_string[0:len(is_prefix)] == is_prefix else 0

print(solution("banana","banananan"))

# 다른사람풀이
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))