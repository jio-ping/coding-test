"""문자열 계산하기"""
def solution(my_string):
    my_string = my_string.split(" ")
    count = int(my_string[0])
    for i in range(1,len(my_string)):
        if i %2 !=0:
            my_string[i+1]=my_string[i]+my_string[i+1]
        else:
            count +=int(my_string[i])
    return count
    
        

print(solution("1 + 3 - 5"))

# 다른사람풀이 
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))