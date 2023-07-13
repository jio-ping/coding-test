'''완주하지 못한 선수'''
def solution(participants, completion):
    not_complete = ""
    for participant in participants:
        if participant in completion:
            completion.remove(completion[completion.index(participant)])
        else:
            not_complete+=participant
    return "".join(not_complete)

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))