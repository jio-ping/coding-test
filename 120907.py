"""OX퀴즈"""
def solution(quiz):
    expression = []
    result =[]
    for q in quiz:
        expression.append(q.split("="))
    for i in range(0,len(expression)):
        if eval(expression[i][0]) == int(expression[i][1]):
            result.append("O")
        else:
            result.append("X")
    return result
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))

# 다른사람풀이
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]    