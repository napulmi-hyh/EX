"""
회문(Palindrome) 검사 - deque 사용

핵심 포인트
- deque: 양쪽에서 빠르게 데이터를 꺼낼 수 있음 (popleft, pop)
- isalnum(): 문자와 숫자만 True (공백, 특수문자 제거)
"""

from collections import deque

def is_palindrome(s: str) -> bool:
    
    chars = deque()   # deque 생성 (함수 안에서 생성해야 매번 초기화됨)

    # 문자/숫자만 남기고 소문자로 변환
    for char in s:
        if char.isalnum():
            chars.append(char.lower())

    # 앞/뒤 비교
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False

    return True


if __name__ == "__main__":         # 이 파일을 “직접 실행했을 때만” 아래 코드를 실행하라
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
