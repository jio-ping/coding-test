"""암호회독"""
def solution(ciphers,code):
    answer = []
    for i in range(1,len(ciphers)+1):
        if i % code ==0:
            answer.append(ciphers[i-1])
    return "".join(answer)

print(solution("dfjardstddetckdaccccdegk",4))

# 다른사람풀이
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
