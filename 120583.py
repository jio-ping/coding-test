"""중복된 숫자 개수"""
def solution(array,n):
    count = 0
    for arr in array:
        if str(n) == str(arr):
            count +=1
    return count

print(solution([1,2,3,4,1],1))

# 다른사람풀이

def solution(array, n):
    return array.count(n)