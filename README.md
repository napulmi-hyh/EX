# PYTHON
 Fighting
# 알고리즘 공부 기록

파이썬 알고리즘 인터뷰 책 기반으로 공부 중

## 📘 String
1. - palindrome.py : 팰린드롬 검사
     (return은 함수 안에서만 사용/ self는 클래스에서만 사용 /  타입힌트는 실행과 관계없음/ pop(0)은 느리다)
    - palindrome_deque.py   : deque- 양쪽에서 빠르게 데이터를 꺼낼 수 있음 (popleft, pop)
     (strs=deque() 객체생성 / strs:Deque 설명 / strs:Deque = deque() 생성과 설명)
    - palindrome_re.py
   (1. 소문자로 변환 / 2. 문자/숫자만 남김 / 3. 문자열 뒤집기 4. 비교)
2. - reverseString  (1. 투포인트를 이용한 스왑 2. reverse)
3. - reorderLogFile (1. 문자로그가 숫자로그 앞에 2. 가장 앞은 식별자
                      3. 문자가 동일한경우 식별자 순, 4. 숫자로그는 순서대로)/ lambda 매개변수:반환값
4. most Common Word - 가장 흔한 단어
         1. 정규식 문자 정리 : re.sub()문자열 치환 함수/ [^\w] 문자 숫자,밑줄 제외 모든문자
         2. 리스트 컴프리핸션 : [word for word in ~ if word not in banned]
         3. 단어 개수 세기 : collections.Counter(words) : 각 단어가 몇 번 나왔는지 자동으로 세줌
         4. counts.most_common(1) 가장 많이 나온 단어 1개 반환- 결과 : [('ball', 2)]
         5. 단어만 꺼내기 [0][0] 첫번째요소("hello",2) / 그중 단어("hello")
## 📘 Array
- (추가 예정)

## 공부 기록
- GitHub 사용 시작
- 문자열 문제 풀이 시작
