"""인덱스 바꾸기"""
def solution(my_string, num1, num2):
    answer = []
    for i in range(len(my_string)):
        if i == num1:
            answer.append(my_string[num2])
        elif i == num2:
            answer.append(my_string[num1])
        else:
            answer.append(my_string[i])
    return "".join(answer)
print(solution("hello",1,3))

# 다른사람풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
