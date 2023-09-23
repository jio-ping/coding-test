# 체육복
def solution(n,losts,reserves):
    여벌가진사람= set(reserves)-set(losts) 
    # print(여벌가진사람)
    잃어버린사람 = set(losts)-set(reserves) 
    # print(잃어버린사람)
    for i in 여벌가진사람:
        if i-1 in 잃어버린사람:
            잃어버린사람.remove(i-1)
        elif i+1 in 잃어버린사람:
            잃어버린사람.remove(i+1)
    return(n-len(잃어버린사람))

print(solution(5,[1,2,3],[2, 3, 4]))
"""
for i in range(len(reserve)):
        if reserve[i] or reserve[i]-1 or reserve[i]+1 in have_training:
            if have_training[reserve[i]] == False:
                have_training[reserve[i]] = True
            elif have_training[reserve[i]-1] == False:
                have_training[reserve[i]-1] =True
            elif have_training[reserve[i]+1] ==False:
                have_training[reserve[i]+1]=True
        print(have_training)
"""
# 다른사람풀이
def soldution(n, lost, reserve): 
    answer = 0 
    
    reserve_del = set(reserve)-set(lost) 
    lost_del = set(lost)-set(reserve) 
    
    for i in reserve_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
            
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
            
    answer = n - len(lost_del)
    
    return answer
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)