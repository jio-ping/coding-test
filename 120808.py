"""분수의 덧셈"""

from fractions import Fraction
def solution(numer1,denom1,numer2,denom2):
    answer = Fraction(numer1,denom1)+Fraction(numer2,denom2)
    return [answer.numerator, answer.denominator]
print(solution(1,2,3,4))


#  모듈 안 쓰고 다른사람풀이 
def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1*num2) +(denum2*num1)
    num0 = num1*num2

    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer
