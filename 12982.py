# 예산
def soltuion(d,budget):
    total = 0
    cnt =0 
    for dept in sorted(d):
        if budget > total + dept : 
            total += dept
            cnt +=1
    return cnt

print(soltuion([2,2,3,3],10)) 
# 다른사람풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)