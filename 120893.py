"""대문자와 소문자"""
def solution(my_string):
    answer = []
    for string in my_string:
        if string.isupper():
            answer.append(string.lower())
        else:
            answer.append(string.upper())
    return "".join(answer)


# 다른사람풀이
def solution(my_string):
    return my_string.swapcase()

