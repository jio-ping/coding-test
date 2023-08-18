# 부족한금액계산하기
def solution(price,money,count):
    return sum([ i*price for i in range(1,count+1)]) - money if sum([ i*price for i in range(1,count+1)]) - money >0 else 0
        
print(solution(3,20,1))