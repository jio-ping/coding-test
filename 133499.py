# 옹알이(2)
def solution(babblings ):
    can_speak = ["aya","ye","woo","ma" ]
    answer = []
    for babbling in babblings:
        for canspeak in can_speak:
            if not (f'{canspeak+canspeak}') in babbling:
                babbling=babbling.replace(canspeak,"1")
        answer.append(babbling)
    return len([ans for ans in answer if ans.isdigit()])
print(solution(  ["ayayeye"]))

# 다른사람풀이

def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
