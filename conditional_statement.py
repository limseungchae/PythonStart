# 조건문
# 사용자로부터 상품의 가격을 입력받는다.
price = int(input("상품의 가격:"))

# 배송비를 결정한다.
if price > 20000 :
    shipping_cost = 0
else:
    shipping_cost = 3000

# 배송비를 출력한다
print("배송비 =", shipping_cost)
print("-------------------------------------")
# 논리 연산자
# x and y 모두가 참이면 참 아니면 거짓
# x or y 둘중 하나가 참이면 참 모두 거짓이면 거짓
#not x x가 참이면 거직,x가 거짓이면 참
price = 25000  # 상품의 가격
card = "python"  # 결제 카드

if price > 20000 and card == "python":
    print("조건에 해당됩니다.")
else:
    print("조건에 해당되지 않습니다.")
print("-------------------------------------")
# 조건 연산자
numbers = [-10, 5, 8, 3, 12, 6]

# 절대값 계산 : 음수이면 반대로 변환한 값
abs_numbers = [abs(num) for num in numbers]

# 최대값 계산
max_value = max(numbers)

# 최소값 계산
min_value = min(numbers)

print("원본 숫자:", numbers)
print("절대값:", abs_numbers)
print("최대값:", max_value)
print("최소값:", min_value)

# 조건 연산자2
x = int(input("첫 번째 수 ="))
y = int(input("두 번째 수 ="))
max_value = (x if x > y else y)
min_value = (y if x > y else x)
print("큰 수=",max_value, "작은 수=", min_value)
print("-------------------------------------")

# 이프로그램은 산수 문제를 출제한다
# f-문자열을 사용한다. 변수를 {  }로 감싸서 문자열 안에 넣을
# 앞에 f를 붙인다.
import random

x = random.randint(1, 100)
y = random.randint(1, 100)

answer = int(input(f"{x} + {y} = "))

# 부울 변수에 결과를 저장하고 출력한다.
flag = (answer == (x+y))
print(flag)
print("-------------------------------------")

# 동전 던지기 게임
import random

print("동전 덩지기 게임을 시작합니다.")
coin = random.randrange(2) # 0 아니면 1
if coin == 0 :
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")
print("-------------------------------------")

# 아이디 찾기
id = "ilovepython"
s=input("아이디를 입력하시오:")
print(f"{s}!")
if s == id:
#    print(f"{s}!!")
    print("환영합니다.")
else:
    print("아이디를 찾을 수 없습니다.")
#    print(f"({s})아이디를 찾을 수 없습니다.")
print("-------------------------------------")