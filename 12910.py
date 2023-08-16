# 나누어 떨어지는 숫자 배열
def solution(arr,divisor):
    answer = []
    for ar in arr :
        if ar%divisor==0:
            answer.append(ar)
    if len(answer)>0:
        return sorted(answer)
    else:
        return [-1]
print(solution([2, 36, 1, 3],1	))

# 다른사람풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]