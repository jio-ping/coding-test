# 대충만든자판
def solution(keymap, targets):
    dictionary = {}
    answer = []
    for target in targets:
        cnt = []
        for spell in target:
            if spell in dictionary:
                # cnt += dictionary[spell]
                cnt.append(dictionary[spell])
            else:
                find_index =  [km.index(spell) for km in keymap if spell in km] 
                if find_index != []:
                    dictionary[spell] = min(find_index)+1
                    # cnt += dictionary[spell]
                    cnt.append(dictionary[spell])
                else:
                    answer.append(-1)
        if -1 not in cnt:
            answer.append(sum(cnt))
        else:answer.append(-1)
    return answer

print(solution(["AA"],["B"]	))
print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))
print(solution(["BC"], ["AC", "BC"]))