"""배열의 유사도"""
def solution(arr1, arr2):
    count = 0
    duplicated_list = []
    for arr in arr2:
        if arr in arr1 and arr not in duplicated_list:
            duplicated_list.append(arr)
            count+=1
    return count

print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]))
# 다른사람풀이
def solution(s1, s2):
    return len(set(s1)&set(s2))
