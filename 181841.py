# 꼬리문자열
def solution(str_list,ex):
    return "".join([str for str in str_list if ex not in str])


print(solution(["abc", "bbc", "cbc"],"c"))

# 다른사람풀이
def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))