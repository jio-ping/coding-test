# ad 제거하기
def solution(strArr):
  return [str for str in strArr if "ad" not in str]

print(solution(["and","notad","abcd"]))