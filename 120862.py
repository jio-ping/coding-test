"""최댓값만들기(2)"""
def solution(numbers):
    numbers=sorted(numbers)
    return max(numbers[-2]*numbers[-1],numbers[0]*numbers[1])

print(solution([0, -31, 24, 10, 1, 9]))