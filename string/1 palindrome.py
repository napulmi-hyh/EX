"""
문제: 유효한 팰린드롬

설명:
- 문자열에서 알파벳과 숫자만 남긴다
- 대소문자를 구분하지 않기 위해 모두 소문자로 변환
- 앞과 뒤를 비교해서 같은지 확인

내가 한 실수:
- return을 함수 밖에서 사용해서 오류 발생
- self를 함수에서 사용하려고 해서 오류 발생
- 타입힌트 때문에 실행 안 된다고 착각 (실제 원인은 self)

시간복잡도:
- O(n) (문자열을 한 번 순회)
"""

# 문자열 정리: 문자/숫자만 남기고 소문자로 변환
def isPalindrome(s:str)->bool:
    strs=[]
    for char in s:
        if char.isalnum():
            strs.append(char.lower())


# 양쪽 비교 (팰린드롬 검사)
    while len(strs)>1:
        if strs.pop(0) != strs.pop():
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
