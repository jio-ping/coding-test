# # 둘만의 암호
# def solution(str, skips, index):
#     alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     strindex = []
#     answer = []
#     for s in str:
#         strindex.append(alphabet.index(s))
#     for strdex in strindex: 
#         count = 0
#         for skip in skips:
#             if skip in alphabet[strdex:strdex+index+1]:
#                 count+=1
#         # if count + strdex +index< 26:
#         #     answer.append(alphabet[count+strdex+index])
#         # else:
#         answer.append(alphabet[(count+strdex+index)%26])
#     return ("".join(answer))

# def solution(str,skips,index):
#     alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     answer = []
#     for skip in skips:
#         del(alphabet[alphabet.index(skip)])
#     for s in str:
#         if alphabet.index(s) + index < len(alphabet):
#             answer.append(alphabet[alphabet.index(s)+index])
#         else:
#             answer.append(alphabet[(alphabet.index(s)+index)%len(alphabet)])
#     return("".join(answer))




# 다른사람 풀이
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result

print(solution(s="zukvwh",
skip="bcxtmq"
,index=5))

