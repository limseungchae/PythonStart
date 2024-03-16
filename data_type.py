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