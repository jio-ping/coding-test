# 시저암호
def solution(s,n):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    answer = []
    for ss in s:
        if ss.islower():
            ss = ss.upper()
            answer.append(alphabet[alphabet.index(ss)+n-26].lower())
        elif ss == " ":
            answer.append(" ")
        else:
            answer.append(alphabet[alphabet.index(ss)+n-26])
    return "".join(answer)
print(solution("AB",1))

# 다른사람풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)