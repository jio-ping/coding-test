# 최댓값과 최솟값
def solution(s):
    numbers=[ int(number) for number in s.split(" ")]
    return f'{min(numbers)} {max(numbers)}'

print(solution("1 2 3 4"))


# 다른사람풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

