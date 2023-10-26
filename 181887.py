# 홀수 vs 짝수
def solution(num_list): 
    # cnt = 짝수번재 숫자의 총합 
    cnt = sum( num_list[i] for i in range(len(num_list)) if i%2 ==0)
    # num_list의 총합 - 짝수 총합 = 홀수 총합 
    return sum(num_list)-cnt if sum(num_list) - cnt > cnt else cnt

print(solution([4, 2, 6, 1, 7, 6]))