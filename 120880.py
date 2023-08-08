# 특이한 정렬
def solution(numlist, n):
    result = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return result

        
print(solution([1, 2, 3, 4, 5, 6],4))

    # while len(sort_index_list)>0:
        
    #         answer.insert(0,numlist[sort_index_list.index(max(sort_index_list))])
    #         sort_index_list.remove(max(sort_index_list))