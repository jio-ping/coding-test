"""숫자찾기"""
def solution(num,k):
    return str(-num).find(str(k))

print(solution(29183,3))

# 다른사람풀이
def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1