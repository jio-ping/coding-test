# 길이에 따른 연산
from functools import reduce
def solution(num_list):
    if len(num_list) >=11:
        return(sum(num_list))
    else:
        return reduce(lambda x,y : x*y,num_list)
    
print(solution([2, 3, 4, 5]))
# 다른사람풀이
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))

from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)