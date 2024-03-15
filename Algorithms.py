# 반지름 20인 원의 면적 = 1256.0 / 파이 = 3.14 x r x r

# 알고리즘
# 1 . 사용자로 부터 원의 반지름을 입력받는다.
# 2. 공식을 적용하여 면적을 계산한다.
# area = radius * radius * p
# 3. 면적을 화면에 출력한다.

# 코드
# 변수 radius에 값을 저장한다
radius = 10

# 공식을 적용하여 면적을 계산한다 - 둘중 아무거나 써도 가능
area1 = 3.14 * radius * radius
area2 = 3.14 * radius ** 2

#면적을 화면에 출력한다.
print("1반지름",radius, "인원의 면적=", area1)
print("2반지름",radius, "인원의 면적=", area2)
