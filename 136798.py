# 기사단원무기
def solution(number,limit,power):
    count_divisor = []
    while number >0:
        cnt =0
        for i in range(1, int(number**(1/2)) + 1):
            if (number % i == 0):
                cnt += 1
                if ( (i**2) != number) : 
                    cnt += 1     
        if cnt> limit : 
            count_divisor.append(power)
        else:
            count_divisor.append(cnt)
        number -= 1
    return sum(count_divisor)
print(solution(10,3,2))