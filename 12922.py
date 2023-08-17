# 수박수박수박수박수박수?
def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])
print(solution(3))

# 다른사람풀이
def water_melon(n):
    return "수박" * (n//2) + "수" * (n%2)


