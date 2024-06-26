# 횟수 제어 반복
# 제어문

# 조건문
# 연봉이 2500 이상이면 취업하고 아니면 고시 준비해야지

# 반복문
# 토익 점수가 600을 넘을 때까지 반복해서 공부해야지

# 반문의 환영합니다! 5번 반복
print("반문의 환영합니다!")
print("반문의 환영합니다!")
print("반문의 환영합니다!")
print("반문의 환영합니다!")
print("반문의 환영합니다!")

# 반문의 환영합니다! 5번 반복 for문
for i in range(5):print("반문의 환영합니다!")

# 반복의 종류

# 조건 반복(while문)
# 특정한 조건이 성립되는 동안 반복
# 기록이 1촏 단축될 때까지 반복하세요.

# 횟수 반복(for문)
# 정해진 횟수만큼 반복
# 트랙을 10바퀴 뛰세요.

# 횟수 반복
# 반복의 횟수를 미리 아는경우에 사용
# for 변수 in 시퀀스: 문장
# 시퀀스에 항목이 있는가?
# 시퀀스의 다음 할목 문장을 싱행한다.
# 시쿼스에 더 이상 항목이없으면 종료

# 조건반복
# 특정한 조건이 만족되는 동안 계속 반복
# 조건이 거짓이면 끝
# 조건이 참이면 문장을 실행한다.

# 리스트란?
# 항목들을 저장하는 자료 구조
# 영어 = 0, 수학 = 1, 사회 = 2, 과학 = 3
slist=["영어","수학","사회","과학"]
print(slist)

# 리스트에 동적으로 항목 추가
list = []       # 공백 리스트를 생성한다.
list.append(1)  # 리스트에 정수 1을 추가한다.
list.append(2)  # 리스트에 정수 2을 추가한다.
list.append(6)  # 리스트에 정수 6을 추가한다.
list.append(3)  # 리스트에 정수 3을 추가한다.

print(list)     # 리스트를 출력한다.

# 리스트의 인덱스
# 인데스는 0부터 시작
# 첫번째 항목으ㅟ 인덱스는 0
# 두번째 항목으ㅟ 인덱스는 1
# 세번째 항목으ㅟ 인덱스는 2
slist=["영어","수학","사회","과학"]
print(slist[0]) # 영어

# 리스트 항목 변경
slist=["영어","수학","사회","과학"]
slist[-1] = "컴퓨터"   # ['영어', '수학', '사회', '컴퓨터']
print(slist)

# 회수 제어 반복 - for문
# range() 함수 - 종료값까지 생성

# 연속 계산
sum = 0
n = 10
# for i in range(1, n+1) :
for i in range(n,0,-1) :
    # sum = sum + i
    sum += i
    print(f"{i},{sum}")
print("합=",sum)

# 구구단 계산
for i in range(1,10) :
    print("9 *",i,"=", 9*i)

# 사용자로 부터 숫자를 받아서 팩토리얼 계산
# 예를 들어, 5 팩토리얼은 다음과 같이 계산됩니다:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
n = int(input("정수를 입력하시오:"))
fact = 1
# for i in range(1, n+1):
for i in range(n,0,-1):
    # fact = fact * i
    fact *= i
    print(f"{i} {fact}")
print(n,"!은",fact,"이다.")


# turtle 그리기 - 원하는 수 각형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","몇각형을 원하시나요?:")
n = int(s)

for i in range(n):
    t.forward(100)
    t.left(360/n)

turtle.done()

# 조건 제어 반복
# 조건 제어 반복읒 어떤 조건이 만족 되는 동안 반복
# (예) 투자금이 목표에 도달하는 기간을 계산
# 투자금 < 목표금액 → 이자를 계산한다. → 이자를 투자금에 더한다. → year를 증가한다.

# while문
# 제어 변수를 선언한다.
i = 1
sum = 0

# i 값이 10보다 작으면 반복
while i <= 10:
    sum =sum + i
    i = i + 1
print("합계는",sum)

# 숫자 맞추기 게임
# 시도 횟수
# 사용자의 추측값
# 1 과 100 사이의 난수
import random
tries = 0
guess = 0;
answer = random.randint(1,100)
print("1부터 100 사이의 숫자를 맞추시오")
while guess != answer:
    guess=int(input("숫자를 입력하시오:"))
    tries = tries + 1
    if guess < answer:
        print("너무 낮음!")
    elif guess > answer:
        print("너무 높음!")
if guess == answer:
    print("축하합니다. 시도 횟수=",tries)
else:
    print("정답은",answer)

# 패스워드 맞추기
password = ""
while password != "pythonisfun" :
    password = input("암호를 입력하시오:")
print("로그인 성공")

# 중첩 반복문
# 반복 루프 안에 다시 반복 루프

# 사각형 패턴 출력하기
for i in range(5):
    for x in range(10):
        print("*", end="")
    print("")

# 무한 루프와 break, continue
# while True:
#   if 조건:
#       break   # 반복을 중단한다.
#   if 조건:
#       continue # 다음 반복을 시작한다.

# 신호등 예제
# 신호등 색상을 입력하시오 red
# 신호등 색상을 입력하시오 yellow
# 신호등 색상을 입력하시오 green
# 전진!!
while True:
    light = input("신호등 색상을 입력하시오")
    if light == "green":
                break
print("전진!!")

# 이 프로그램은 중첩 반복문을 사용하여서 모든 조합을 출력한다.
coffee = ["Americano", "Latte", "Mocha"]
cake = ["CheeseCake","StrawberryCake", "ChocolateCake"]

for co in coffee:
    for ca in cake:
        print(co + "" + ca)

# 3의 배수이면
# 다음 반복을 시작한다.
# 줄바꿈을 하지 않고 스페이스만 출력한다.
for i in range(1,11):
    # if i%3 == 0:
    # if i%2 == 0:
    # if i%2 != 0:
    if i%2 == 1:
        continue
        print(i,end="")