# k번째 수
def solution(array,commands):
    return([sorted(array[comm[0]-1:comm[1]])[comm[2]-1] for comm in commands])

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 다른사람풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))