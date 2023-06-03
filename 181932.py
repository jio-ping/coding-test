"""코드처리하기"""

def solution(code):
    mode = 0
    answer = []
    for i in range(len(code)):
        if code[i] != "1":
            if mode == 0 and i%2==0:
                answer.append(code[i])
            elif mode == 1 and i%2!=0:
                answer.append(code[i])
        else:
            if mode == 0:
                mode = 1
            elif mode ==1:
                mode= 0
    return "".join(answer) if answer !=[] else "EMPTY"

print(solution("abc1abc1abc"))


# 다른사람풀이
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"