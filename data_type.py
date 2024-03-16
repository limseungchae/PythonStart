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

