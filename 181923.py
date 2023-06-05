"""수열과 구간 쿼리 2"""
# def solution(arr, queries):
#     answer = []
#     for query in queries:
#         k = query[2]
#         temp = []
#         for i in range(query[0],query[1]+1):
#             if arr[i] > k:
#                 temp.append(arr[i]) 
#         if temp != []:        
#             answer.append(sorted(temp)[0])
#         else:
#             answer.append(-1)
#     return answer

# 다른사람풀이
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

print(solution([0,1,2,4,3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))