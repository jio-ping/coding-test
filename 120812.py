"""최빈값구하기"""
def solution(array):
    count_dict = {}
    answer = 0
    answer_count = 0 
    for arr in list(set(array)):
        count_dict[arr] = array.count(arr)
    
    for key in count_dict.keys():
        if count_dict[key] > answer_count:
            answer = key
            answer_count = count_dict[key]
        elif count_dict[key] == answer_count:
            answer = -1
    return answer

print(solution([1, 2,2, 2, 3, 3, 3,4,4,4,4]))

# 다른사람풀이
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1