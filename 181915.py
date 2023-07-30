# 글자이어붙여문자열만들기
def solution(my_string, index_list):
    answer = [my_string[idx] for idx in index_list]
    return "".join(answer)

print(solution("cvsgiorszzzmrpaqpe",[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))