# 옹알이

def solution(babbling):
    speaking = {'aya':0,'ye':1,'woo':2,'ma':3}
    baby_saying = {Value:Key for Key,Value in speaking.items()}
    answerlist = []
    sayinglist = []
    answer = 0
    for b in babbling:
        for s in speaking:
            b = b.replace(f'{s}',f"{speaking[s]}",1)
        if b.isdigit():
            answer += 1
            answerlist.append(b)
            for a in answerlist:
                for i in range(0,4):
                    a = a.replace(f"{i}",f"{baby_saying[i]}") 
            sayinglist.append(a)
    print(f'my baby said {str(sayinglist)[1:-1]} T_T ♡')
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))


# 다른사람풀이
def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c