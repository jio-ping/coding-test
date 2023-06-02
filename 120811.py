"""중앙값 구하기"""
def solution(array):
    array = sorted(array)
    return array[(len(array)//2)]
print(solution([9,-1,0]))

# 다른사람풀이

def solution(array):
    return sorted(array)[len(array) // 2]
