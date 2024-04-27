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

