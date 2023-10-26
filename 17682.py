# 1차 다트게임
def solution(dartResult):

    table = { "*":"*2+",
             "#":"*-1+",
            "S":"*1+",
             "D":"**2+",
             "T":"**3+",
             "+*":"*",
             }
    for key,value in table.items():
        dartResult =  dartResult.replace(key,value)
        print((dartResult))
    print(eval(dartResult[:-1]))
print(solution("	1D#2S*3S"))