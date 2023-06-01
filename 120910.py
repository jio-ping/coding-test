"""세균증식"""
def solution(n,t):
    answer = n
    if 1<=n<=10 and 1<=t<=15:
        for i in range(0,t):
            answer = answer*2   
        return answer

# 다른사람풀이
def solution(n, t):
    return n*(2**t)