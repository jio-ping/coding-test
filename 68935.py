# 3진법 뒤집기
def solution(n):
    answer = []
    while n != 0:
        answer.append(str(n % 3))
        n = n//3
    return int("".join(answer), 3)


print(solution(45))
