# 자료형(데이터타입)
# 변수는 특정한 자료형의 데이터를 저장할 수 있음
# 자료형에 따라서 허용되는 연산이 달라짐
INTEGER = 10
FLOAT = 3.14
STRING = "hello"

print("정수",INTEGER, "실수",FLOAT, "문자열",STRING)

# 자료형을 알려면?
print(type(1234))  # int
print(type('blue'))  # str
print(type(3.14))  # float
print(type(2 < 3))  # bool
print(type((2, 3, 4)))  # tuple

# 정수형(1)
# 정수형이란?
# 1, -23, 0 등
x = 100 ** 30
print(x)
print(type(x))
