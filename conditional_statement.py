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

