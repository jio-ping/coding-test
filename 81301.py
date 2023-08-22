# 숫자문자열과 영단어
def solution(s):
    table = {"0":"zero",
"1":"one",
"2":"two",
"3":"three",
"4":"four",
"5":"five",
"6":"six",
"7":"seven",
"8":"eight",
"9":"nine"}
    for key,value in table.items():
        if value in s :
            s = s.replace(value,key)
    return s

print(solution("one4seveneight"))

# 다른사람풀이
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)