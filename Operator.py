# 연산자가 아닌 함수로 계산
x = 10
y = 3
quotient, remainder = divmod(x, y)  # divmod 함수를 사용하여 x를 y로 나눈 몫과 나머지를 구합니다.
# divmod 함수는 몫과 나머지를 한 번에 계산하여 튜플 형태로 반환합니다.
# quotient 변수에는 몫이, remainder 변수에는 나머지가 할당됩니다.
print(quotient, remainder)  # 몫과 나머지를 출력합니다. 3  1

# 거듭제곱(power) 계산
# 2의 7승의 계산
a = 2 ** 7
print(a) # 128

# 할당 연산
x = 1  # 변수 x에 1을 할당합니다.
value = 3.0  # 변수 value에 3.0을 할당합니다.
x = (1/2) + 3  # 변수 x에 수식의 결과를 할당합니다.
x = y = z = 0
x, y, z = 10, 20, 30

print(x, y, z)  # 10, 20, 30

# 복합 할당 연산자
# +=처럼 대입 연산자와 다른연사자를 결합한 연산자
x = 5
x += 2  # x = x + 2와 동일합니다.

print(x) # x = 7

# 복합 연산자
# 제일 많이 사용하는 복합 연산자 문장은 x += 1 이다.
x = 1000
x += 2  # x는 1002가 된다.
x -= 2  # x는 다시 1000이 된다.
print(x)

# 복합 연산자 total 값 계산
total_sales = 0
milk_count = int(input("판매된 우유의 개수:"))
cola_count = int(input("판매된 콜라의 개수:"))
krice_count = int(input("판매된 김밥의 개수:"))

total_sales += milk_count * 2000
total_sales += cola_count * 3000
total_sales += krice_count * 3500

print(f"\n오늘 총 매충은 {total_sales}원입니다.")

# 관계 연산자
# 두개의 피연산자를 비교하는데 사용
# "변수 x가 변수 y보다 큰지"를 결정 (==, !=, >, <, >=, <=)

# 부울 변수
radius = 100
flag = (radius > 32)
print(flag) # True

# 20000원 이상이면 배송비 0 원 이하면 3000원
price = float(input("상품의 가격을 입력하세요: "))  # 가격을 입력받음
expensive = price > 20000   # expensive가 부울 변수이다.
if expensive:               # 관계 수식 대신에 부울 변수가 들어가도 된다.
    shipping_cost = 0
else:
    shipping_cost = 3000
print("배송비는", shipping_cost, "원 입니다.")  # 배송비 출력

# 문자열
s1 = "Audrey Hepbyrn"
s2 = "Audrey Hepbyrn"
print(s1 == s2) # True

# 아스키코드 알파벳 순
s1 = "Audrey Hepbyrn"
s2 = "Grace Kelly"
print(s1 < s2) # True

# 비트 연산자
# 정수를 이루고 있는 각각의 비트를 가지고 작업할 수 있는 연산자
# 비트 AND (&): 두 비트가 모두 1이면 결과는 1이 되고, 그렇지 않으면 결과는 0이 됩니다.
# 비트 OR (|): 두 비트 중 하나 이상이 1이면 결과는 1이 되고, 둘 다 0이면 결과는 0이 됩니다.
# 비트 XOR (^): 두 비트가 서로 다르면 결과는 1이 되고, 같으면 결과는 0이 됩니다.
# 비트 NOT (~): 단일 피연산자의 각 비트를 반전시킵니다. 즉, 0은 1로, 1은 0으로 변환됩니다.

# 비트 이동 연산자
# 비트 이동 (<<, >>): 비트를 왼쪽이나 오른쪽으로 이동시킵니다.
# 왼쪽 쉬프트(<<)는 주어진 수만큼 비트를 왼쪽으로 이동하고, 오른쪽 쉬프트(>>)는 오른쪽으로 이동합니다.
a = 0b01101101 # a는 109이다.
print(a<<1, a>>1) # 218 54
print(bin(a<<1),bin(a>>1)) # 0b11011010 0b110110

# 세탁기 비트 연산자 예제 프로그램
# 세탁기의 문이 열려있으면 비트 2가 1
# 비트 2가 0인지 1인지를 검사하는 코드
status = 0b01101110;
print("문열림 상태=",((status & 0b00000100)!=0)) # True

# 연산자의 우선 순위
# 산술 연산자 우선 순위
# 지수 **
# 곱셉 *, 나눗셈/, 나머지 %
# 덧셈 +과 뺼셈-

# 괄호의 사용
1 + 2 * 3   # 7
4 - 40 - 3  # -39
10 + 20/2   # 20.0  # 정수 나눗셈 //
(10 + 20) /2    # 15.0