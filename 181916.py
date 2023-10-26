# 주사위게임
def solution(a,b,c,d):
    dice = sorted([a,b,c,d])
    counts = [dice.count(cnt) for cnt in dice] 
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3: 
        return (10 * dice[counts.index(3)] + dice[counts.index(1)])**2
    elif max(counts) == 2:
        if min(counts) == 2:
            return( dice[1]+dice[2]) * abs(dice[1]-dice[2])
        else:
            return (a*b*c*d)//((dice[counts.index(2)])**2)
    else:
        return min(dice)
        
print(solution(2,5,2,6))

# def solution(a, b, c, d):
#     nums = [a, b, c, d]
#     counts = [nums.count(i) for i in nums]
#     if max(counts) == 4:
#         return a * 1111
#     elif max(counts) == 3:
#         p = nums[counts.index(3)]
#         q = nums[counts.index(1)]
#         return (10 * p + q) ** 2
#     elif max(counts) == 2:
#         if min(counts) == 2:
#             return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
#         else:
#             p = nums[counts.index(2)]
#             return (a * b * c * d) / p**2
#     else:
#         return min(nums)