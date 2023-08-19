# 행렬의 덧셈
def solution(arr1,arr2):
    answer = []

    for i in range(0,len(arr1)):
        tmp = [arr1[i][n]+arr2[i][n] for n in range(len(arr1[i]))]
        answer.append(tmp)
    return answer
print(solution([[1,1]],[[6,5]]))

# 다른사람풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

