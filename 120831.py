def solution(n):
    if n>0:
        if n %2 ==0:
            return solution(n-2) + n
        else:
           return solution(n-1) 
    else:
        return n
        
print(solution(8))

# 다른사람 풀이 
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])