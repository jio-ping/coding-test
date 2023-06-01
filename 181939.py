"""더 크게 합치기"""
def solution(a,b):
   
    if int(str(a)+str(b)) > int(str(b)+str(a)):
        return int(str(a)+str(b))
    else:
        return int(str(b)+str(a))

print(solution(8,91))


#다른사람풀이
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
