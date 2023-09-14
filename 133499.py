# 옹알이(2)
def solution(babblings ):
    can_speak = ["aya","ye","woo","ma" ]
    answer = []
    for babbling in babblings:
        for canspeak in can_speak:
            if not babbling.startswith(f'{canspeak+canspeak}'):
                babbling=babbling.replace(canspeak,"1")
        answer.append(babbling)
    return len([ans for ans in answer if ans.isdigit()])
print(solution(["ayayeayayeaya"]))
# 1
print(solution(  ["yemayemayemayemayemayemayemaye"]))