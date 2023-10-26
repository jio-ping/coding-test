# 로또의 최고 순위와 최저 순위
def solution(lottos,win_nums):
    # 일치한 번호의 개수 : 등수
    result = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt = 0
    for winnum in win_nums:
        if winnum in lottos:
            cnt += 1
    return [result[cnt+lottos.count(0)],result[cnt]]
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))

# 다른사람풀이 
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]