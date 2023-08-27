# 최대 공약수와 최소공배수
# def solution(n,m):
#     tmp = 1
#     for i in range(min(n,m),1,-1):  
#         if n%i ==0 and m%i==0:
#             print(i)
#             n=n//i
#             m=m//i
#             tmp *= i    
#     return ([tmp,int(tmp * n* m)])
      
    
# 다른사람풀이 

def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]


def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer

def gcd(a,b):
    print(a%b)
    if not a%b:
        return b
    else:
        gcd(b,a%b)

print(gcd(76,36))