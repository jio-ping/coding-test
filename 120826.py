"""특정문자제거하기"""
def solution(my_string, letter):
    answer = ""
    for string in my_string:
        if string !=letter:
            answer +=string
    return answer

print(solution("abcdef","b"))

# 다른사람풀이

def solution(my_string, letter):
    return my_string.replace(letter, '')