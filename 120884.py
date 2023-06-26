"""치킨쿠폰"""
def solution(chicken):
    coupon = chicken
    service_chicken = 0
    while coupon >= 10:
        service_chicken += 1
        coupon -= 9
    return service_chicken
print(solution(100))

# 다른사람풀이
def solution(chicken):
    answer = 0
    while(chicken>=10):
        answer+=1
        chicken-=9
    return answer