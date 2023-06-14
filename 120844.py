"""배열회전시키기"""

def solution(numbers,direction):
    answer =[]
    if direction == "right":
        answer.append(numbers[-1])
        answer+=numbers[0:-1]
    else:
        answer += numbers[1:]
        answer += numbers[0:1]
        
    return answer

print(solution([1,2,3,4],"left"))

# 다른사람풀이
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]