"""7의개수"""
def solution(array):
    answer = 0
    array = "".join(str(array))
    for i in range (len(array)):
        if array[i] == "7":
            answer+=1
    return answer
print(solution([7, 77, 17]))

# 다른사람풀이
def solution(array):
    return ''.join(map(str, array)).count('7')
