# 이진수 더하기
def solution(bin1,bin2):
    return format(int(f'0b{bin1}', 2) + int(f'0b{bin2}', 2),'b')
print(solution(10,11))