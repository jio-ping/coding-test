# 약수의 개수와 덧셈
import math
def solution(left,right):
    sum = 0
    for i in range(left,right+1):
        if math.sqrt(i).is_integer():
            sum -= i
        else:
            sum+= i
    return sum

print(solution(13,17))

# 다른사람풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer