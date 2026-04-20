"""
Palindrome Check using Regular Expression and Slicing

문자열이 회문(Palindrome)인지 확인하는 함수
- 대소문자 구분 없음
- 공백, 특수문자 제거 후 비교
"""

import re   #정규식 import

def is_palindrome(s: str) -> bool:
    s = s.lower()

    # [^a-z0-9] → 소문자와 숫자가 아닌 모든 문자 제거,e.sub() — “바꿔서 결과만 반환”/subn - 결과, 몇번바꿨는지
    s = re.sub('[^a-z0-9]', '', s)

    # s[::-1] → 문자열 역순
    return s == s[::-1]


# 직접 실행할 때만 테스트 코드 실행
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
