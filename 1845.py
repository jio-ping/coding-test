# 폰켓몬
def solution(nums):
    ponketmon = {}
    for num in nums:
        if num not in ponketmon:
            ponketmon[num] = nums.count(num)
    return len(ponketmon) if len(nums)//2 > len(ponketmon) else len(nums)//2

print(solution([3,3,3,2,4,2]))

# 다른사람풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
