# 상수(constant)
# 한번 값이 결정되면 절대로 변경되지 않는 변수
# 파이썬에서 통상적으로 대문자로 상수를 표현 // 그렇다고 변경 안되는 것은 아님
TAX_RATE = 0.35
PI = 3.141592
MAX_SIZE = 100

INCOME = 1000
TAX_RATE = 0.35

# 소득과 소득세율이 변경되었다면 상수의 정의만 변경
tax = INCOME * TAX_RATE
net_income = INCOME - tax