'''완주하지 못한 선수'''
# 효율성 0 점 
def solution(participants, completion):
    not_complete = ""
    for participant in participants:
        if participant in completion:
            completion.remove(completion[completion.index(participant)])
        else:
            not_complete+=participant
    return "".join(not_complete)

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

import collections

# 다른사람풀이 
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]