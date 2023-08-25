# 푸드 파이트 대회
def solution(food):
    tmp = []
    final = []
    answer = []
    for i in range(1,len(food)):
        tmp.append(food[i]//2)
    i = 1
    for ans in tmp:
        while ans != 0:
            final.append(str(i))
            ans -= 1
        i+=1
    answer = answer+final
    answer.append("0")
    for fin in reversed(final):
        answer.append(str(fin))
    return "".join(answer)

print(solution([1,3,4,6]))

"""어우 너무 구질구질하게 풀음 ;;새로 풀어보자"""

# 다른사람풀이

def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer