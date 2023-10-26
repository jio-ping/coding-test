# 문자열바꿔서찾기
def solution(myString,pat):
    return int((pat.replace("A","C").replace("B","A").replace("C","B") ) in myString)
print(solution("ABBAA","AABB"))