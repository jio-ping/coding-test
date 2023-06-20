"""가까운 수"""
def solution(array,n):
    minus = []
    for arr in sorted(array):
        minus.append(abs(n-arr))
    print(minus)
    return sorted(array)[minus.index(min(minus))]

print(solution([10, 14, 12],13))
# 다른사람풀이 
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]
