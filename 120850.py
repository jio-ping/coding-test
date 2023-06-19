"""문자열 정렬하기(1)"""
def solution(my_string):
    answer = []
    for string in my_string:
        try:
            answer.append(int(string))
        except:pass
    return sorted(answer)
print(solution("hi12392"))
# 다른사람풀이
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])