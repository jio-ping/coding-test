# 추억점수
def solution(name,yearning,photos):
    score_dict = {}
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
    answer = []
    for photo in photos:
        score = 0 
        for people in photo:
            if people in score_dict:
                score += score_dict[people]
        answer.append(score)
    return answer

print(solution(["kali", "mari", "don"],[11, 1, 55],[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))

# 다른사람풀이
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]
