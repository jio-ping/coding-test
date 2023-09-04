# 조건에 맞게 수열 변환하기 1
def solution(arr):
    answer =[] 
    for ar in arr :
        if ar >= 50 and ar%2 ==0:
            answer.append(ar//2)
        elif ar<50 and ar%2!=0:
            answer.append(ar*2)
        else:
            answer.append(ar)
    return answer


print(solution([1,2,3,100,99,98]))

# 다른사람풀이

def solution(arr):
    return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]