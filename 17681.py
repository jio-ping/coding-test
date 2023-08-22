# 비밀지도
def solution(arr1,arr2,n):
    binary_arr = []
    answer =[]
    for i in range(0,n):
        tmp  = bin ( arr1[i] | arr2[i])[2:].zfill(n)
        binary_arr.append(tmp)
    for binary in binary_arr:
        answer.append(binary.replace("0b","").replace("1","#").replace("0"," ").zfill(n))
    return answer
    
print(solution([9, 20, 28, 18, 11],[30, 1, 21, 17, 28],5))

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i] | arr2[i])[2:].zfill(n)
        b = a.replace("1", "#").replace("0", " ")
        answer.append(b)
    return answer