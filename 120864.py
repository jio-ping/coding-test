"""숨어있는 숫자의 덧셈(2)"""
def solution(my_string):
    temp = "0"
    answer = 0
    for string in my_string:
        if string.isdigit():
            temp += string
        else:
            answer += int(temp)
            temp = "0"
    answer+= int(temp)
    return answer

print(solution("1a2b3c4d123Z"))

# 다른사람풀이

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())