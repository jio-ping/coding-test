# 체육복
def solution(n,losts,reserves):
    have_training = {}
    for i in range(1,n+1):
        if i in losts and i not in reserves:
            have_training[i] = False
        else:
            have_training[i] = True
    for reserve in reserves:
        if have_training[reserve] == False:
            have_training[reserve] = True
        elif reserve-1 in have_training and have_training[reserve-1] ==False:
            have_training[reserve-1] = True
        elif reserve+1 in have_training and have_training[reserve+1] ==False:
            have_training[reserve+1] = True
        
    return len([value for key,value in have_training.items() if value == True ])

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
def solution(n, lost, reserve): 
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