"""2차원으로 만들기"""
# def solution(num_list, n):
#     answer =[]
#     while not num_list ==[]:
#         answer.append(num_list[:n])
#         num_list = num_list[n:]
#     return answer
# 런타임에러.....

def solution(num_list,n):
    answer =[] 
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:i+n])
    return answer
print(solution([1,2,3,4,5,6,7,8,9,10],3))