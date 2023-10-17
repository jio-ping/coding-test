# 전국대회선발고사

def solution(rank,attendance):
    can_attendant = filter(lambda x: attendance[rank.index(x)] != False, rank)
    can_attendant =  sorted(list(can_attendant))
    return can_attendant[0] * 10000 + can_attendant[1] * 100 + can_attendant[2]
print(solution([3, 7, 2, 5, 4, 6, 1],[False, True, True, True, True, False, False]))