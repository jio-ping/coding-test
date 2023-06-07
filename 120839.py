"""가위바위보"""
def solution(rsp):
    cheet = {"0":"5","2":"0","5":"2"}
    return "".join([cheet[r] for r in rsp])
print(solution("205"))

# 다른사람 풀이 

def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
