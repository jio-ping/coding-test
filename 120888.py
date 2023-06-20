"""중복된 문자 제거"""
def solution(string):
    answer = []
    for str in string:
        if str not in answer:
            answer.append(str)
    return "".join(answer)

print(solution("We are the world"))

# 다른사람풀이
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))