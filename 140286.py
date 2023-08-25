# 가장가까운같은글자
def solution(s):
    alpha = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in alpha:
            answer.append(-1)
        else:
            answer.append(i-alpha[s[i]])
        alpha[s[i]] = i
    return answer
    
print(solution("foobar"))
