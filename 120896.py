"""한 번만 등장한 숫자"""
def solution(my_string):
    alphabet = {}
    for string in my_string:
        if string not in alphabet:
            alphabet[string] = 1
        else:
            alphabet[string]+=1
    return "".join(sorted([k for k, v in alphabet.items() if v == 1]))
print(solution("adfvgd"))

# 다른사람풀이
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer