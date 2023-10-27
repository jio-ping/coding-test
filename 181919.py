# 콜라츠 수열 만들기
def solution(n):
  answer =[]
  while n != 1:
    answer.append(n)
    if n%2 ==0:
      n //=2
      print(n)
    else:
      n = 3*n +1 
  answer.append(n)
  return answer

print(solution(10))