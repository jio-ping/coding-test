"""잘라서 배열로 저장하기"""
def solution(my_str,n):
    answer = []
    while len(my_str) > n:
        answer.append(my_str[:n])
        my_str = my_str[n:]
    answer.append(my_str)
    return answer

print(solution("abcdef123",3))
# 다른사람풀이
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]