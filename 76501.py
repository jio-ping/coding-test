# 음양 더하기
def solution(absolutes,signs):
    tmp = 0
    for i in range(0,len(absolutes)):
        if signs[i]>0:
            tmp += absolutes[i]
        else:
            tmp -= absolutes[i]
    return tmp

print(solution([4,7,12],[True, False, True]))

# 다른사람풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
