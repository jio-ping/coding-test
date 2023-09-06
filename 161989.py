# 덧칠하기
def solution(n, m, section):
    answer = 1 
    paint = section[0]
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer

print(solution(4,1,[1,2, 3, 4]))
print("_____")
print(solution( 4, 2, [3, 4]))
print("_____")
print(solution(8,4,[2, 3, 6]))
print("_____")
print(solution(5,5,[3]))

# 시간초과
def time_out_solution(n,m,section):
    cnt  = 0
    while len(section) > 1:
        for i in range(min(section),max(section)+1,m):
            if i in section:
                section.remove(i)
                cnt += 1
    return cnt

# 다른사람풀이
def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer