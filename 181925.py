"""수 조작하기(2)"""
def solution(numLog):
    result = ""
    control={1:"w",-1:"s",10:"d",-10:"a"}
    for i in range(1,len(numLog)):
        result += control[numLog[i]-numLog[i-1]]
    return result
print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))