# 햄버거 만들기
def solution(ingredient):
    cnt = 0
    total_ingredient = "".join([str(i) for i in ingredient])
    while "1231" in total_ingredient:
        find_index = total_ingredient.find("1231")
        if find_index != -1:
            cnt += 1
            total_ingredient = total_ingredient[:find_index] + \
                total_ingredient[find_index+4:]
    return cnt


print(solution([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3,
      1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))
