# 같은 숫자는 싫어
def solution(arr):
    answer = []
    for ar in arr : 
        if len(answer) ==0 or answer[-1] != ar:
            answer.append(ar)
    return(answer)

print(solution([4,4,4,3,3]))

# 다른사람풀이
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a