# 문자열 나누기
def solution(string): 
    cnt = 0
    answer = []  
    while len(string)>0:
        
        if cnt == 0 :
            tmp = []
            standard = string[0]
            tmp.append(standard)
            cnt += 1
            string = string[1:]
            answer.append(tmp)
        elif standard == string[0]:
            cnt += 1
            tmp.append(string[0])
            string = string[1:]
        else:
            cnt-=1 
            tmp.append(string[0])
            string = string[1:]
    print(answer)


print(solution("aaabbaccccabba"))

            
