#자연수 뒤집어 배열로 만들기 
def solution(n):
    return [ int(str(n)[len(str(n))-i-1])for i in range(len(str(n)))]


print(solution(54321))
# 다른사람풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))