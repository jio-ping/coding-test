"""배열 원소의 길이"""
def solution(strlist):
    answer =[]
    for str in strlist:
        answer.append(len(str))
    return answer
print(solution(["We", "are", "the", "world!"]))

# 다른사람풀이

def solution(strlist):
    answer = list(map(len, strlist))
    return answer
