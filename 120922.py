"""종이자르기"""
def solution(M,N):
    answer = 0
    cnt = 0
    if M and N != 1:
        for i in range(1,M):
            answer += 1
        for b in range(1,N):
            cnt += 1
        answer += (M)*cnt
    return answer

print(solution(2,5))

# 다른사람풀이
def solution(M, N):
    return (M * N) - 1

def get_cut_cnt_dfs(width, height):
    width, height = min(width, height), max(width, height)

    if width == 1 and height == 1:
        return 0

    return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)

def solution(M, N):
    return get_cut_cnt_dfs(M, N)