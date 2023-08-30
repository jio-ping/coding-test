# 2016년
def solution(a,b):
    calendar = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    day_of_the_week=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    day = 0
    for i in range(1,a):
        # 1/1 ~ a전 달 마지막 날까지 더함 
        day += calendar[i]
    day += b 
    return day_of_the_week[day%7-1]

print(solution(5,24))

# 다른사람풀이
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]