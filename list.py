# 리스트란
# 항목(item)들을 저장하는 컨테이너로서 그 안에 항목들이 순서를 가지고 저장됨
# 어떤 타입의 항목라도 저장 가능

# 리스트 사용하는 예
# 지난 1주일 중에서 가장 더운 날 찾기
# 월,화,수,목,금,토,일
# 0,1,2,3,4,5,6
# temps = 리스트, 항목 = [28, 31, 33, 35, 27, 26, 25]
temps = [28, 31, 33, 35, 27, 26, 25]

# 리스트 인덱스(index)
# 리스트에서의 항목의 위치(번호)
# 0부터 시작
temps = [28, 31, 33, 35, 27, 26, 25]
print(temps[3]) # 35

# 리스트 요소 변경
temps = [28, 31, 33, 35, 27, 26, 25]
temps[3] = 36
print(temps[3]) # 36

# 인덱스 오류
# 인덱스를 사용할 때는 인덱스가 적정한 범위에 잇는지를 항상 신경 써야 함
temps = [28, 31, 33, 35, 27, 26, 25]
# temps[7] = 36
# IndexError: list assignment index out of range

# 리스트 정렬(1)
# 순서대로 정렬할때
# sort()
a = [3, 2, 1, 5, 4]
a.sort()
print(a)     # [1,2,3,4,5]

# 역순으로 정렬할때
a = [3, 2, 1, 5, 4]
a.sort(reverse=True)
print(a)     # [5,4,3,2,1]

# 리스트 정렬(2)
# sorted()
numbers = [10,3,7,1,9,4,2,8,5,6]
ascending_numbers = sorted(numbers)
print(ascending_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 요소 추가하기
# 새로운 요소를 리스트의 맨 끝에 추가
# append()
fruis = []              # 공백 리스트를 생성한다.
fruis.append("apple")   # 리스트에 "apple"을 추가한다.
fruis.append("banana")  # 리스트에 "banana"를 추가한다.
print(fruis)    # ['apple', 'banana']

# 지정된 위치에 요소를 추가
# insert()
fruis = ['apple', 'banana', "grape"]
fruis.insert(1,"cherry")
print(fruis) # ['apple', 'cherry', 'banana', 'grape']

# 리스트 탐색하기
fruis = ['apple', 'banana', "grape"]
n = fruis.index("banana")  # n은 1이 된다.
if "banana" in fruis:
    print(fruis.index("banana"))    # 1

# 요소 삭제하기
# 항목이 저장된 위치를 알고 있다면
# pop(i)을 사용
fruis = ['apple', 'banana', "grape"]
item= fruis.pop(0) # "apple" 이 삭제된다.
print(fruis) # ['banana', 'grape']

# 항목의 값만 알고 있다면
# remobve(value)
fruis = ['apple', 'banana', "grape"]
fruis.remove("banana") # "banana" 이 삭제된다.
print(fruis) # ['apple', 'grape']

# remove(
# 만약 삭제하고자 하는 항목이 없다면 오류(예외)가 발생
heroes = ["아이언맨","토르","헐크"]
heroes.remove("토르")

# 확인후 삭제
if "토르" in heroes:
    heroes.remove("토르")
print(heroes) # ['아이언맨', '헐크']

# 리스트 연산 정리
# 리스트 생성:
# 리스트를 생성할 때는 대괄호([])를 사용하고 각 요소는 쉼표(,)로 구분합니다.
# 예: my_list = [1, 2, 3, 4, 5]
# 요소 접근:
# 인덱싱을 사용하여 리스트의 특정 위치에 있는 요소에 접근할 수 있습니다.
# 예: first_element = my_list[0]
# 요소 변경:
# 인덱싱을 사용하여 리스트의 특정 위치에 있는 요소를 변경할 수 있습니다.
# 예: my_list[0] = 10
# 리스트 길이:
# len() 함수를 사용하여 리스트의 길이(요소 개수)를 구할 수 있습니다.
# 예: length = len(my_list)
# 리스트 추가:
# append() 메서드를 사용하여 리스트의 끝에 새로운 요소를 추가할 수 있습니다.
# 예: my_list.append(6)
# 리스트 연장:
# extend() 메서드를 사용하여 리스트의 끝에 다른 리스트의 모든 요소를 추가할 수 있습니다.
# 예: my_list.extend([7, 8, 9])
# 리스트 삽입:
# insert() 메서드를 사용하여 리스트의 특정 위치에 새로운 요소를 삽입할 수 있습니다.
# 예: my_list.insert(2, 100)
# 요소 삭제:
# remove() 메서드를 사용하여 리스트에서 특정 값을 가진 첫 번째 요소를 삭제할 수 있습니다.
# 예: my_list.remove(3)
# 리스트 슬라이싱:
# 슬라이싱을 사용하여 리스트의 일부분을 추출할 수 있습니다.
# 예: sub_list = my_list[1:4]
# 리스트 복제:
# 리스트를 복제할 때는 슬라이싱을 사용하거나 copy() 메서드를 사용합니다.
# 예: new_list = my_list[:] or new_list = my_list.copy()

# 성적리스트 처리하기
STUDENTS = 5
lst = []
count = 0

for i in range(STUDENTS):
    value = int(input("성적을 입력하시오: "))
    lst.append(value)

print("\n성적 평균 =", sum(lst) / len(lst))
print("최대점수 =", max(lst))
print("최소점수 =", min(lst))

for score in lst:
    if score >= 80:
        count += 1

print("80점 이상 =", count)

scores = [10.1, 9.0, 8.3, 7.1, 3.0, 9.0]

#------------------------------------------
print("제거전:", scores)

scores.remove(max(scores)) # 최대값 제거
scores.remove(min(scores)) # 최소값 제거
len(scores) # 수 4
sum(scores)/len(scores) # 평균 8.35
sum(scores) # 합 33.4

print("제거후:", scores)
#------------------------------------------
# 리스트 합병과 복제
fruits1 = ["apple", "chjerry"]
fruits1 = ["banana", " blueberry"]
fruis = fruis1 + fruits2
# ["apple", "chjerry", "banana", " blueberry"]
numbers = [1,2,3] * 3 # [1,2,3,1,2,3,1,2,3]
numbers = [0] * 12 #[0,0,0,0,0,0,0,0,0,0,0,0]

# 리스트 비교
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)   # True

list1 = [3,4,5]
list2 = [1,2,3]
print(list1 > list2)   # True

# 리스트 얕은 복사하기
temps = [28,31,33,35,27,26,25]
value = temps
print(temps)    # temps 리스트 출력
value[3] = 39   # values 리스트 변경
print(temps)    # temps 리스트가 변경되었다.
# [28,31,33,35,27,26,25]
# [28,31,33,39,27,26,25]

# 리스트 깊은 복사하기
temps = [28,31,33,35,27,26,25]
value = list(temps)
print(temps)    # temps 리스트 출력
value[3] = 39   # valuies 리스트 변경
print(temps)    # temps 리스트가 변경 안됨
# [28,31,33,35,27,26,25]

# 슬라이싱(slicing)
# 리스트의 일부를 잘라서 추출하는 기법
# 리스트에서 numbers[2:7]
# 인덱스 2부터 시작하여 인덱스 7이 나오기 전까지 추출
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 인덱스 0부터 시작하여 인덱스 3이 나오기 전까지 추출 (즉, 인덱스 0, 1, 2의 요소)
print(numbers[:3])  # 출력: [10, 20, 30]
# 인덱스 3부터 시작하여 끝까지 추출 (즉, 인덱스 3부터 끝까지의 요소)
print(numbers[3:])  # 출력: [40, 50, 60, 70, 80, 90]
# 리스트 전체를 추출
print(numbers[:])   # 출력: [10, 20, 30, 40, 50, 60, 70, 80, 90]
# 리스트를 복제하여 새로운 리스트를 생성
new_numbers = numbers[:]

# 리스트 변경
# 리스트 일부변경
lst = [1,2,4,5,6,7,8]
lst[0:3] = ["white","blue","red"]
lst # ["white","blue","red",4,5,6,7,8]

# 99 를 중간에 추가
lst = [1,2,4,5,6,7,8]
lst[::2] = [99,99,99,99]
lst # [99,2,99,4,99,6,99,8]

# 리스트의 모든 요소 삭제
lst = [1,2,4,5,6,7,8]
lst[:] = []
lst # []

# 리스트 특정요소 삭제
numbers = list(range(0,10)) # 0에서 시작하여 9까지 저장하는
print(numbers)

del numbers[-1] # 마지막 항목 삭제
print(numbers)
# [0,1,2,3,4,5,6,7,8,9]
# [0,1,2,3,4,5,6,7,8]