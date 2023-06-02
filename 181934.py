"""조건문자열"""
# ord(">")62
# ord("<")=60
# ord("=")=61
# ord("!")=33

def solution(ineq,eq,n,m):
    if n != m:
        if n>m:
            return int(ord(ineq) == 62)
        elif n<m:
            return int(ord(ineq) == 60)
    else:
        return int(ord(eq) == 61)
    
print(solution(">","=",20,50))

# 다른사람풀이

def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))