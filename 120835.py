"""진료순서정하기"""
def solution(emergency):
    patient = sorted(emergency,reverse=True)
    return [patient.index(i)+1 for i in emergency]
        
print(solution([3,76,23]))

# 다른풀이

def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]