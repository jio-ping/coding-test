"""연속된 수의 합"""

def solution(num,total):
    ans = []
    a = 0
    for i in range(0,num):
        a += i
    x = (total - a)/num
    for i in range(num):
        ans.append(int(x+i))
    return ans

print(solution(3,0))

# 다른사람풀이 
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]