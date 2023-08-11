# 짝수와 홀수
def solution(num):
    return "Even" if num %2 ==0 else "Odd"

# 다른사람풀이 
def evenOrOdd(num):
    if num%2:
        return "Odd"

    return "Even" 

def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]
""" & 가 and bit 연산후 이진수로 마지막 숫자에 (1의 자리에) 1이 있으면 홀수 이니 
True면 1 False면 0을 리턴한뒤 인덱스가 됨 .... 미친 """