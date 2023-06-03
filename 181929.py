"""원소들의 곱과 합"""
def solution(num_list):
    total = 0
    product = 1
    for num in num_list:
        product *=num 
        total += num
    return 1 if product < total**2 else 0

print(solution([3,4,5,2,1]))

