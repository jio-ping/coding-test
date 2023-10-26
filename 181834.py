# ㅣ로 만들기
def solution(myString):
    l_front_alpha = ["a","b","c","d","e","f","g","h","i","j","k"]
    for l_front in l_front_alpha:
        myString=myString.replace(l_front,"l")
    return myString