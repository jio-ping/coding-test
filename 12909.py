# 올바른 괄호
def solution(s):  
    if s[0] != ")" and len(s) % 2== 0 and s[-1] != "(": 
        stack = []
        for braket in s : 
            if braket == "(":
                stack.append(braket)
            elif len(stack) > 1 and braket == ")":
                stack.pop()

        return False if len(stack) > 1 else True
    else:
        return False
# 다른사람풀이
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0

print(solution("(()("))
print(solution("()()"))