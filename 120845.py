"""공던지기"""
def solution(numbers,k):
    number_list = numbers*(1000//len(numbers))
    answer = []
    for i in range(0,2*k,2):
        answer.append(number_list[i])
    return answer[-1]
print(solution([1,2,3],3))