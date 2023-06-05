"""수 조작하기1"""
def solution(n,control):
    control_count = (control.count("w")*1 + control.count("s")*-1 + control.count("d")*10 +control.count("a")*-10)
    return n + control_count

print(solution(0,"wsdawsdassw"))

# 다른사람풀이 
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])