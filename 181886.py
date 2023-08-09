# 5명씩
def solution(names):
    return [names[i] for i in range(0,len(names),5)]

# 다른사람풀이
def solution(names):
    return names[::5]