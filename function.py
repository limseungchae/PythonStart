# 함수(function)
# 특정 작업을 수행하는 명령어들의 모음에 이름을 붙인 것
# 작업에 필요한 데이터를 전달받을 수 있으며,
# 작업이 완료된 후에는 작업의 결과를 호출자에게 반환 가능
# 입력 -> 함수 -> 출력

# 함수를 사용하는 경우
# 함수를 이용하면 우리가 여러 번 반복해야 되는 처리 단계를 하나로 모아서 필요할 때
# 언제든지 호출하여 가능

# 함수정의
def greet():
    print("안녕하세요!")

greet()  # 함수 호출

# 함수 호출(function call)
# 함수의 이름을 써주는 것(get_area())
# 함수가 호출되면 함수 안에 있는 문장들이 실행되며 실행이 끝나면
# 호출한 위치로 되돌아 감
def get_area(width, height):
    area = width * height
    return area

result = get_area(5, 3)
print("사각형의 넓이:", result)

# 함수는 여러번 호출 가능
# 일단 작성되면 몇 번이라도 호출이 가능
# 첫 번째 호출
result1 = get_area(5, 3)
print("사각형 1의 넓이:", result1)

# 두 번째 호출
result2 = get_area(10, 4)
print("사각형 2의 넓이:", result2)

# 세 번째 호출
result3 = get_area(7, 7)
print("사각형 3의 넓이:", result3)

