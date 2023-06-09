"""구슬을 나누는 경우의 수"""
def solution(balls, share):
    balls_prev = 1
    for i in range (balls,1,-1):
        balls_prev = balls_prev*i
    
    shares_prev = 1
    for i in range(share,1,-1):
        shares_prev*=i 
    
    ball_mi_share=balls-share
   
    ball_share=1
    for i in range(ball_mi_share,1,-1):
        ball_share*=i
   
    return balls_prev//(ball_share*shares_prev)

print(solution(3,2))

# 다른사람의 풀이
import math
def solution(balls, share):
    return math.comb(balls, share)