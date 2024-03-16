# 자료형(데이터타입)
# 변수는 특정한 자료형의 데이터를 저장할 수 있음
# 자료형에 따라서 허용되는 연산이 달라짐
INTEGER = 10
FLOAT = 3.14
STRING = "hello"

print("정수",INTEGER, "실수",FLOAT, "문자열",STRING)

# 자료형을 알려면?
print(type(1234))  # <class 'int'>
print(type('blue'))  # <class 'str'>
print(type(3.14))  # <class 'float'>
print(type(2 < 3))  # <class 'bool'>
print(type((2, 3, 4)))  # <class 'tuple'>

# 정수형(1)
# 정수형이란?
# 1, -23, 0 등
x = 100 ** 30
print(x)
print(type(x))

# 정수형(2)
# 다양한 진법 가능
a = 0xFF    # 16진수
b = 0o77    # 8진수
c = 0b1111  # 2진수
print(a,b,c) # 모든변수를 10진수로 출력한다.
# 255 63 15

# 부동소수점형이란?
# 실수를 나타내는 자료형
a = 3.14
b = 1.23e2  # e는 지수부를 의미 1.23e2는 1.23*102
print(a,b)
# 3.14 123.0

a = 3.14
b = 7.12
print(a+b, a-b, a*b, a/b)

# 문자열
# 문자들의 시퀀스 - 문자가 순서대로 나오는것
greeting = "Merry Christmas!"
print(greeting) # 출력 시에는 항상 작은 따옴표 이용

greeting = 'Happy New Year!'
print(greeting)

message = "철수가 '안녕'이라고 말했습니다."
print(message)  # 문자열 안에 따옴표를 넣을때는 다른형태의 따옴표를 사용

greeting = '''지난한해 저에게 보여주신 보살핌과 사랑에 깊음 감사를 드립니다. 새해에도 하시고자 하는일 모두 성취하시기를 바랍니다.'''
print(greeting) # 여러 줄로 된 문자열은 '''...'''을 사용

# 문자열 <-> 수치값
# str()
# 수치값을 문자열로 바꿈
price_str = str(123)
height_str = str(3.14)

# int()
# 문자열을 정수로 변경
price_int = int("123")

# float()
# 문자열을 실수로 변경
height_float = float("3.14")

print(price_str, height_str)
print(price_int, height_float)

# 문자열의 반복
# * 연산자 사용
line = "=" * 50
print(line)
# ==================================================
message = "Congratulations! "
print(message*3)
# Congratulations! Congratulations! Congratulations!

# 문자열 메소드
# len()
# 문자열의 길이를 계산
message = "Merry CHristmas!"
print(len(message)) # 16

# upper()와 lower()
# 문자열을 대문자나 소문자로 변경
message_upper = message.upper()
message_lower = message.lower()
print(message_upper)  # "MERRY CHRISTMAS!"
print(message_lower)  # "merry christmas!"

# fiond()
# 문자열에서 어떤 단어를 찾음
# 위치는 0부터 시작하는 인덱스로 반환
message_find = message.find("CH")
print(message_find) # 6

# 문자열 안의 문자에 접근하기
# 문자열
# 여러 개의 문자로 이루어짐
s = "Python"
print(s[0])  # 'p' # 첫 번째 문자
print(s[1])  # 'y' # 두 번째 문자
print(s[-1])  # 'n' # 마지막 문자

# 문자열 안에 변수 출력
# f-문자열(f-string)
# 문자열 안에 출력하고 싶은 변수를 중괄호로 감싸서 넣는 방법
price = 10000
print(f"상품의 가격은 {price}원 입니다.")

product = "coffee"
count = 3
price = 10000
print(f"상품{product} {count}개의 가격은 {count*price}원입니다.")

pi = 3.141592
print(f"원주률={pi:2f}") # 소수점 두번째 자리까지 출력
