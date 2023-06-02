"""자릿수 더하기"""
def solution(n):
    answer = 0
    parameter_list = [n for n in str(n)]
    for parameter in parameter_list:
        answer += int(parameter)
    return answer

# 다른사람풀이 
def solution(n):
    answer = sum(list(map(int,list(str(n)))))
    return answer


