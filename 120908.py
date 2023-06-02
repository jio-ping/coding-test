"""문자열 안에 문자열"""

def solution(str1,str2):
    if str1.find(str2)>=0:
        return 1
    else:
        return 2
    
# 다른사람풀이
def solution(str1, str2):
    return 1 if str2 in str1 else 2