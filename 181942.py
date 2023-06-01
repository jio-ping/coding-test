"""문자열 섞기"""
def solution(str1,str2):
   answer =[]
   for i in range(1,len(str1+str2)+1):
      if i%2 !=0:
        answer.append(str1[0])
        str1 = str1[1:]
      else:
        answer.append(str2[0])
        str2 = str2[1:]
   return "".join(answer)
      
# 다른사람풀이 
def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer