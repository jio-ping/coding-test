"""배열 두배 만들기"""
def solution(numbers):
    return list(map(lambda x: x*2,numbers))
print(solution([1, 2, 3, 4, 5]))