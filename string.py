# 문자열 처리하기
# 컴퓨터는 근본적으로 숫자를 처리하는 기계
# 인간을 상대하여야 하기 떄문에 텍스트를 처리하는 작업 중요

# 파이썬의 문자열 처리 기능
# 문자열 함수들을 이용하여 텍스트데이터를 수정,보완 가능
# 텡스트 데이터에는 대소문자가 섞여 있을 수 잇고, 문자열의 앞뒤에 필요 없는 공백 문자가 붙어 있을 수 있음
# BeautifulSoup과 같은 우수한 라이브러리들도 제공
# 쉽게 텍스트를 처리 가능

# 문자열
# 문자열은 문자들의 시퀀스로 정의
# 글자들이 실(string)로 묶여 있는것이 문자열
# s1 = 'Hello'
# s2 = "Hello"
# 따옴표 안에 따옴표가 있는 경우
# s3 = "This isK im's dog."
# 이스케이프 문자로 작은 따옴표 표시
# s3 = 'This is Kim\'s dog.'

# 원시 문자열
# 문자열의 시작 따옴표 앞에 r
# 백슬래시를 이스케이프 문자로 취급하지 않음
print(r'This is Kim\'s dog.')
# This is Kim\'s dog.
# 원시 문자열은 r'C:\User\Kim\Document'와 같은 윈도우 파일 경로를 나타내는 문자열에 필요

# 인덱싱
# 문자열 시퀀스(sequence)라는 자료 구조에 속함
s = 'Monty Python'
print(s[0])     # M
print(s[-1])    # n

# 슬라이싱
#문자열의 일부를 잘라서 서브 문자열 만드는 연산
s = 'Monty Python'
print(s[6:10])     # Pyth   # 여러 문자 선택

t = s[:-1]  # Monty Pytho   # 마지막 문자 삭제
print(t)

t = s[-2:]  # on            # 종료 인덱스 생략
print(t)

s =s[:2]    # Mo
print(s)

# in과 not in 연산자
print('Hello' in 'Hello World')     # True
print('WORLD' in 'Hello World')     # False
print('WORLD' not in 'Hello World') # True

# 문자열 안에 문자열 넣기
# + 연산자를 사용하여 작업
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)     # Hello, Alice!

# %s 기호를 두고 이 기호를 %뒤의 값으로 바꾸는 방법
name = "Bob"
greeting = "Hello, %s!" % name
print(greeting)     # Hello, Bob!

# f-문자열 사용
name = "David"
greeting = f"Hello, {name}!"
print(greeting)     # Hello, David!
