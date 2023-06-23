"""영어가 싫어요"""
replace_table ={
"zero":"0",
"one":"1",
"two":"2",
"three":"3",
"four":"4",
"five":"5",
"six":"6",
"seven":"7",
"eight":"8",
"nine":"9"}
def solution(string):
    for replace in replace_table:
        if replace in string:
            string = string.replace(replace,replace_table[replace])
    return int(string)

# 다른사람풀이
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))