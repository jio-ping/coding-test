"""등수매기기"""
def solution(scores):
    sum_score = sorted([sum(score) for score in scores],reverse=True)
    return [sum_score.index(sum(score))+1 for score in scores]
    
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))