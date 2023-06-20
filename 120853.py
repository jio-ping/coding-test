"""컨트롤제트"""
def solution(string):
    string = [str for str in string.split(" ") ]
    string.reverse()
    count = 0

    while len(string) != 0:
        if string[0].lstrip("-").isdigit():
            count += int(string[0])
            string = string[1:]
        else:
            string = string[2:]
    return count        


# 다른사람풀이
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer

print(solution("10 Z 20 Z 1"))
