"""외계어 사전"""
def solution(spell,dic):
    for term in dic:
        if sorted(term) == sorted(spell):
            return 1
    return 2
    
print(solution(["p", "o", "s"],["pos", "eocd", "qixm", "adio", "soo"]))

# 다른사람풀이
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2