# 문자열 내 마음대로 정렬하기
def solution(string,n):
    string=[str[n]+str for str in string]
    return [ss[1:] for ss in sorted(string)]
print(solution(["abce", "abcd", "cdx"],2))

# 다른사람풀이
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])
strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))