# 문자열 뒤의 n글자
def solution(my_string,n):
    answer =[] 
    for i in range(1,n+1):
        answer.insert(0,my_string[-i])
    return "".join(answer)
print(solution("ProgrammerS123",11))

# 다른사람풀이
def solution(my_string, n):
    return my_string[-n:]