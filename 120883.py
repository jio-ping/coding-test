"""로그인성공"""

def solution(id_pw,db):
    db=dict(db)
    if id_pw[0] in db and db[id_pw[0]] == id_pw[1]:
        return "login"
    elif id_pw[0] in db and db[id_pw[0]] != id_pw[1]:
        return "wrong pw"
    else:
        return "fail"

print(solution(["meodseugi", "1w234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))

# 다른사람풀이

def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"