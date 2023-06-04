"""짝수홀수개수"""
def solution(num_list):
    even_count = 0
    for num in num_list:
        if num %2 ==0:
            even_count+=1
    return [even_count, len(num_list)-even_count]

print(solution([1,2,3,4,5]))

# 다른사람풀이
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
