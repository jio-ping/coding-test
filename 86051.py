# 없는숫자더하기
def solution(numbers):
    return 9+8+7+6+5+4+3+2+1 - sum(numbers)

print(solution([1,2,3,4,6,7,8,0]))

# 다른사람풀이
solution = lambda x: sum(range(10)) - sum(x)