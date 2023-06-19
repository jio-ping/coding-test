"""숨어있는 숫자의 덧셈"""
def solution(my_string):
    count = 0
    for string in my_string:
        if string.isdigit():
            count += int(string)
    return count

print(solution("aAb1B2cC34oOp"))

# 다른사람풀이
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())