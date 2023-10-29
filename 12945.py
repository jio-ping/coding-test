# 피보나치 수 
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(5))

def fibs():
    a,b = 0,1   
    a,b = b, a+b
    yield a


def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList

fib(5)