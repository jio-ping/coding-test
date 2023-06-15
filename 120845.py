"""주사위의 개수"""
import math
def solution(box,n):
    return (math.floor(box[0]/n)*math.floor(box[1]/n)*math.floor(box[2]/n))

print(solution([10,8,6],3))