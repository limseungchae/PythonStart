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
