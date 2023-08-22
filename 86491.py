# 최소직사각형
def solution(sizes):
    sizes =[sorted(size) for size in sizes]
    width,length = zip(*sizes)
    return max(width) * max(length)
    
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

# 다른사람풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)