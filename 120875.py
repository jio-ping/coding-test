"""평행"""
def solution(dots):
    answer = 0

    if (dots[0][0] - dots[1][0])/(dots[0][1] - dots[1][1]) == (dots[2][0] - dots[3][0])/(dots[2][1] - dots[3][1]): # 01 23
        answer = 1
    elif (dots[0][0] - dots[2][0])/(dots[0][1] - dots[2][1]) == (dots[1][0] - dots[3][0])/(dots[1][1] - dots[3][1]): # 02 13
        answer = 1
    elif (dots[0][0] - dots[3][0])/(dots[0][1] - dots[1][1]) == (dots[2][0] - dots[3][0])/(dots[2][1] - dots[3][1]): # 03 12
        answer = 1
    else:
        answer = 0  
    return answer
