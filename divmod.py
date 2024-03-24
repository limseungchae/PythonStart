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