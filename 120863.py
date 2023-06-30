"""다항식 더하기"""
def solution(polynomial):
    polynomial = polynomial.split(" ")
    temp = 0
    temp2 = 0
    for poly in polynomial:
        if poly.isdigit():
            temp += int(poly)
        elif "x" in poly:
            if poly[0] == "x":
                temp2+=1
            else:
                temp2+=int(poly[:-1])
    if temp2 > 1:
        if temp == 0:
            return f'{temp2}x'
        elif temp != 0:
            return f'{temp2}x + {temp}'
    elif temp2 == 1:
        if temp == 0 :
            return f'x'
        else:
            return f'x + {temp}'
    elif temp2 == 0:
        return f'{temp}'
    
print(solution("1 + 112x + 3"))

# 다른사람풀이
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'