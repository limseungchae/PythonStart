# 삼각형 그리기
import turtle
t = turtle.Turtle()

t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

turtle.done()

# 사각형 그리기
# 이 프로그램은 사용자로부터 크기를 받아서 사각형을 그린다.
import turtle
t = turtle.Turtle()

s = input("원하시는 모양은[cicle,turtle,square,arrow...]?")
t.shape(s) # 거북이 모양 "cicle","turtle","square","arrow"....
d = input("원하시는 모양의 색상[red,green,blue...]?")
t.color(d) # 거북이 색상 "red","green","blue"....
f = input("펜 색상[red,green,blue...]?")
t.pencolor(f) # 펜 색상 "red","green","blue"....
g = int(input("사각형의 펜의 두께는? "))
t.pensize(g) # 펜 두께

# 사용자로부터 사각형의 크기를 받아서 size라는 변수에 저장한다.
# 사각형의 크기는 정수이므로 input()이 반환하는 문자열을 int()를 통하여 정수로 변환하였다.
size = int(input("사각형의 크기는 얼마로 할까요? "))

# 사각형을 다음과 같은 코드로 그린다. 이떄 변수 size를 사용하자.
t.forward(size)     # size 만큼 거북이를 전진시킨다.
t.right(90)         # 거북이를 오른쪽으로 90도 회전시킨다.
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

turtle.done()
