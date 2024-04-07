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
for i in range(1, n+1) :
    sum = sum + i
print("합=",sum)