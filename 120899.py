"""가장 큰 수 찾기"""
def solution(array):
    return [max(array),array.index(max(array))]

print(solution([1,2,3,4,5,8,1]))