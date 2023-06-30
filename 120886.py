"""A로 B만들기"""
def solution(before,after):
    for bef in before:
        if before.count(bef) != after.count(bef):
            return 0
    return 1

print(solution("allpe","apple"))

# 다른사람풀이
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0