# 커피심부름
def solution(orders):
    sum = 0
    for order in orders:
        if "americano" in order or "anything" == order:
            sum += 4500
        elif "cafelatte" in order:
            sum += 5000
    return sum 