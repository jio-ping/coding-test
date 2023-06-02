"""평행"""
def solution(dots):
    if ((dots[0][1] - dots[1][1])  //( dots[0][0] - dots[1][0]) ) == (( dots[2][1] - dots[3][1] )//( dots[2][0] - dots[3][0] )):
        return 1
    elif (( dots[0][1] - dots[2][1])  // (dots[0][0] - dots[2][0] )) == (( dots[1][1] - dots[3][1]) // (dots[1][0] - dots[3][0] )):
        return 1
    elif (( dots[0][1] - dots[3][1]) // (dots[0][0] - dots[3][0] )) == ((dots[1][1] - dots[2][1] )// (dots[1][0] - dots[2][0] )):
        return 1
    else:
        return 0

print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))