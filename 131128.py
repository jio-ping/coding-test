# 숫자짝꿍
def solution(X,Y):
    X = sorted([x for x in X])
    Y = sorted([y for y in Y])

    answer = ""
    print(X,Y)
    if len(X) < len(Y):
        for x in X:
            if x in X: 
                print(answer)
                answer.add(x)
                Y.remove(x)
                X.remove(x)
    else:
        for i in range(len(Y)):
            if Y[i] in X:
                answer+= Y[i]
                X.remove(Y[i])
                Y.remove(Y[i])
                

    return answer 


print(solution("12321","42531"))
"""
def solution(X,Y):
    answer = []
    X = [x for x in X]
    Y = [y for y in Y]
    print(X)
    print(Y)
    if len(X) <= len(Y):
        for x in X :
            if x in Y:
                answer.append(x)
                X.remove(x)
                Y.remove(x)
    else:
        for y in Y:
            if y in X:
                answer.append(y)
                X.remove(y)
                Y.remove(y)
    return "".join(answer) if len(answer)>0 else -1
"""