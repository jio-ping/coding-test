"""수열과 구간쿼리3"""
def solution(arr, queries):
    answer = arr
    for query in queries:
        arr[query[0]],arr[query[1]] = arr[query[1]],arr[query[0]]
    return(answer)

print(solution([0,1,2,3,4],[[0,3],[1,2],[1,4]]))


# 다른사람 풀이 
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr
