"""등수매기기"""
def solution(scores):
    sum_score = [sum(score[0],score[1]) for score in scores]
    