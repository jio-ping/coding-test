# 하샤드수
def solution(n):
    temp = 0
    for i in str(n):
        temp += int(i)
    return n%temp ==0 

print(solution(13))

# 다른사람풀이 
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0