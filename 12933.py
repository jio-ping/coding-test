# 정수 내림차순으로 배치하기
def solution(param):
    return int("".join(sorted([n for n in str(param)],reverse=True)))



print(solution(118372))