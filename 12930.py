# 이상한 문자 만들기
def solution(string):
    string = string.split(" ")
    answer = []
    for str in string:
        for i in range(len(str)):
            if i %2 == 0:
                answer.append(str[i].upper())
            else:
                answer.append(str[i].lower())
        answer.append(" ")
    return "".join(answer[:-1])

print(solution( "try hello world"))

# 다른사람풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))