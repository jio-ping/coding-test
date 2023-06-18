vowels =["a","e","i","o","u"]
def solution(my_string):
    return "".join([string for string in my_string if string not in vowels])
print(solution("bus"))