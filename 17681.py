# 비밀지도
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:].zfill(n)
        tmp = tmp.replace("1", "#").replace("0", " ")
        answer.append(tmp)
    return answer
    
print(solution([9, 20, 28, 18, 11],[30, 1, 21, 17, 28],5))

# 다른사람풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer