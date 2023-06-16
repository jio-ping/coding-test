# """공던지기"""
def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1

#  이전 풀이 ㅋㅋ
def solution(numbers,k):
    number_list = numbers*(1000//len(numbers))
    answer = []
    for i in range(0,2*k,2):
        answer.append(number_list[i])
    return answer[-1]