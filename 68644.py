# 두개뽑아서 더하기
from itertools import combinations
def solution(numbers):
    comb_list =combinations(numbers,2)
    return sorted(list(set([comb[0]+comb[1] for comb in comb_list])))
        
print(solution([1,1]))

# 다른사람풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))