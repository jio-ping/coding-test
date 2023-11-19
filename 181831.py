# 특이한 이원 배열
def solution(arr):
    answer = 1

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] != arr[j][i]:
                answer = 0

    return answer


print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
