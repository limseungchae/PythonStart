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
