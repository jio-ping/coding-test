# 직사각형 별찍기
a,b= map(int, input().strip().split(' '))

for i in range(b):
    print("*"*a)

# 다른사람풀이

3
4
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
