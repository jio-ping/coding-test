# 실패율
def solution(N,stages):
    stages = sorted(stages)
    score = {}
    for i in range(1,N+1):
        if i in stages:
            score[i] = stages.count(i)/len(stages)
            # stages에서 i 찾아 삭제 -> 그냥 분모 길이를 선언해놓고 count로 계속 뺐으면 됐을듯 
            del stages[stages.index(i):-( stages[::-1].index(i))]
        else:
            score[i] = 0/len(stages)
    return [quet[0] for quet in (sorted(score.items(), key=lambda x: x[1],reverse=True))]
    

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]	))

# 다른사람풀이

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)