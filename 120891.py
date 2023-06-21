def solution(orders):
    three_six_nine = ["3","6","9"]
    count = 0
    for order in str(orders):
        if order in three_six_nine:
            count += 1
    return count

print(solution(3))
# 다른사람풀이
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))