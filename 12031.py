# 자릿수 더하기
def solution(number):
    answer = 0 
    for i in str(number):
        answer += int(i)
    return answer 

# 다른사람풀이
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)