# 가운데글자가져오기
def solution(s):
    return s[len(s)//2] if len(s)%2!=0 else s[len(s)//2 -1 :len(s)//2+1]  

print(solution("sprng"))
# 다른사람풀이
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]