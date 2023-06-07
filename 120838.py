"""모스부호(1)"""
def solution(letters):
    morse = { '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    letter = letters.split(" ")
    return "".join(morse[let] for let in letter) 

print(solution(".... . .-.. .-.. ---"))