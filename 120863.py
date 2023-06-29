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
# temp = 0
#     temp2=""
#     term = 0
    # for poly in polynomial:
    #     if "x" in poly:
    #         temp2+=poly
    #     elif poly.isdigit():
    #         temp += int(poly)
    # print(temp2)
    # for tem in temp2.replace("x","1x"):
    #     if tem.isdigit():
    #         term += int(tem)
    # return f"{term}x + {temp}"
    # list.sort()
    # print(list)
    # print(temp2)

# print(type(3*1))