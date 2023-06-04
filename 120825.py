"""문자 반복 출력하기"""
def solution(my_string, n):
    answer = ""
    for string in my_string:
        answer += string*n
    return answer
print(solution("hell0",3))

# 다른사람풀이
def solution(my_string, n):
    return ''.join(i*n for i in my_string)