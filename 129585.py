"""머쓱이보다 키 큰 사람"""
def solution(array,height):
    if height>0 and height not in array :
        array.append(height)
    array = sorted(array,reverse=True)
    return array.index(height)

# def solution(array,height):
#     count = 0
#     for arr in array:
#         if arr >height:
#             count +=1
#     return count

print(solution([155,142,166,146,178,199],200))