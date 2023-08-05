"""겹치는 선분의 길이"""
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    print(sets[0]&sets[1])
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
print(solution([[0, 5], [3, 9], [1, 10]]))