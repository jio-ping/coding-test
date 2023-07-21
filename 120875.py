"""평행"""
def solution(dots):
    answer = 0

    if (dots[0][0] - dots[1][0])/(dots[0][1] - dots[1][1]) == (dots[2][0] - dots[3][0])/(dots[2][1] - dots[3][1]): 
        answer = 1
    elif (dots[0][0] - dots[2][0])/(dots[0][1] - dots[2][1]) == (dots[1][0] - dots[3][0])/(dots[1][1] - dots[3][1]): 
        answer = 1
    elif (dots[0][0] - dots[3][0])/(dots[0][1] - dots[1][1]) == (dots[2][0] - dots[3][0])/(dots[2][1] - dots[3][1]): 
        answer = 1
    else:
        answer = 0  
    return answer

# 다른사람풀이
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0