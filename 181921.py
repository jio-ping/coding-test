"""배열만들기2"""
import re 
def solution(l,r):
    answer =[ ]
    for i in range(l,r+1):
        if all(num in ['0','5']for num in str(i)):
            answer.append(i)
    if len(answer) ==0 :
        return -1
    return answer

        

print(solution(5,555))


    # for i in range(l,r+1):
    #     if "5" in str(i):
    #         fiveOList.append(i)
    #     elif "0" in str(i):
    #         fiveOList.append(i)
    # if len(fiveOList) == 0:
    #     return -1
    # else:
    #     return fiveOList