# 크레인 인형뽑기 게임
def solution(boards,moves):
    # 2차원 배열 거꾸로 돌려주기 
    real_board = []
    for i in range(5):
        temp = []
        for board in boards:
            if board[i] != 0:
                temp.append(board[i])
        real_board.append(temp)
    print(real_board)
    answer= []
    for move in moves:
        if len(real_board[move-1])!=0:
            answer.append(real_board[move-1][0])
            real_board[move-1] = real_board[move-1][1:]
    print(answer)
    cnt = []
    temp = 0
    for i in range(len(answer)):
        if temp == answer[i]:
            cnt += 1
            del(answer[i-1:i+1])
        else:
            temp = answer[i]
    print(cnt)

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))


# 다른사람풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer