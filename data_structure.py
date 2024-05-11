# 자료구죠
# 자료들을 저장하는 여러가지 구조

# 시퀀스
# 요소로 구성
# 요소 간에는 순서가 있음
# 시퀀스의 요소들은 번호가 붙어 잇음
# 내장 시퀀스(str, bytes, bytearray, list, tuple, rabnge)

# 동일한 연산을 지원
# 인덱싱
# 슬라이싱
# 뎃셈 연산
# 곱셈 연산

# 내장함수 적용가능
# len() - 시퀀스의 길이를 반환
# max() - 최대값
# min() - 최소값

# 튜플(tuple)
# 리스트와는 다르게 듀플은 변경이 불가능
# 문법
# 튜플이름 = (항목1, 항목2,...)
# 공백 튜플 fruiots=()
# 초기값을 가지는 튜플 fruits=("apple","banana","grape")
# 인덱스를 사용하여 요소에 접근 result=fruits[1]

# 튜플 생성
# fruits=("apple","banana","grape")
# fruits="apple","banana","grape"

# 주의할점
# 쉼표가 끝에 있어야 한다.
# 쉼표가 없으면 튜플이 아니라 수식이 된다.
# 튜플의 특성상 만들고 나서 변경이 안된다.

# 튜플 <-> 리스트
# 튜플생성
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)  # 출력: (1, 2, 3, 4, 5)

# 리스트 생성
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)  # 출력: [1, 2, 3, 4, 5]

# 튜플 추가 연산들
# 다른 튜플에 결합
fruits = [1, 2, 3]
fruits += (4, 5, 6)
print(fruits)  # 출력: [1, 2, 3, (4, 5, 6)]

# 리스트에 튜플을 결합
numbers = [1, 2, 3]
numbers += (4, 5, 6)
print(numbers)  # 출력: [1, 2, 3, 4, 5, 6]

# 튜플 패킹과 언패킹
a = 1
b = 2
print("a:", a)  # 출력: a: 1
print("b:", b)  # 출력: b: 2

# 변수 값 교환을 위해 튜플 패킹과 언패킹을 함께 사용합니다.
a, b = b, a
print("a:", a)  # 출력: a: 2
print("b:", b)  # 출력: b: 1

# enumerate() 사용하기
# 함수는 순회 가능한(iterable) 객체(예: 리스트, 튜플, 문자열 등)를
# 입력으로 받아 인덱스와 해당 요소를 포함하는 enumerate 객체를 반환합니다.
fruits = ['apple', 'banana', 'orange']
for index, value in enumerate(fruits):
    print(index,value)
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: orange

# 리스트의 특성
# 문법: 대괄호([]) 사용
# 변경 여부: 변경 가능(mutable),
# 메소드: 요소 추가/삭제/수정 가능
# 용도: 동적 데이터에 사용

# 튜플의 특성
# 문법: 소괄호(()) 사
# 변경 여부: 변경 불가능(immutable),
# 메소드: 요소 수정 불가
# 용도: 정적 데이터에 사용
# --------------------------------------------
# 세트
# 수학에서 배웠던 집합
# 특정 순서로 저장되지 않으며 위치별로 액세스할 수 없음

# 세트 생성하기
# 문법
# 세트 이름 = {항목1, 항목2, ...}
# 초기화된 세트 생성
# numbers = {1,2,3}
# 공백세트 생성
# values = set()