# 조건에 맞게 수열 변환하기 3
def solution(arr,k):    
    if k % 2 ==0:
        return list(map(lambda x: x+k,arr))
    else:
        return list(map(lambda x : x*k ,arr))
    
print(solution([1, 2, 3, 100, 99, 98],3))

# 다른사람풀이
def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]