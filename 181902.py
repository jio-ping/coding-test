# 문자개수세기
def solution(my_string):
    answer = []
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    while len(answer)!=52:
        if len(answer)<len(alphabet):
            for alpha in alphabet:
                answer.append(my_string.count(alpha))   
        else:
            for alpha in alphabet:
                answer.append(my_string.count(alpha.lower()))
    return answer
print(solution("Programmers"))

