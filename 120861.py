"""캐릭터의 좌표"""
def solution(keyinputs, board):
    x,y= 0,0
    answer = (0,0)
    for keyinput in keyinputs:
        if keyinput == "left" and x-1 >= -(board[0]//2):
            x -= 1
        elif keyinput == "right" and x+1 <= board[0]//2:
            x += 1 
        elif keyinput == "down" and y-1 >= -(board[1]//2):
            y -= 1
        elif keyinput == "up" and y+1 <= board[1]//2:
            y += 1
    return x,y

print(solution(["down", "down", "down", "down", "down"],[7, 9]))

# 다른사람풀이
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]



"""if key == "left" and -board[0] //2 <= x-1 < board[0]//2:
            x -= 1
        elif key == "right " and -board[0] //2 <= x+1 < board[0]//2:
            x += 1
        elif key == "up" and -board[1]//2 <= y+1 <= board[1]//2:
            y += 1
        elif key == "down" and -board[1]//2 <= y-1 <= board[1]//2:
            y -= 1"""

"""
x,y = 0,0
    temp =[[-(board[0]//2), board[0]//2],[-(board[1]//2),board[1]//2]]
    
    for key in keyinput:
        if min(temp[0])<=x<=max(temp[0]) and min(temp[1])<=y<=max(temp[1]):
            if key == "left":
                x -= 1
            elif key == "right":
                x += 1
            elif key == "up":
                x += 1
            elif key == "down":
                key -= 1       
        return x,y
"""