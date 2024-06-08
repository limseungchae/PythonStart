# tkinter란?
# 파이썬에서 그래픽 사용자 인터페이스를 개발할때 필요한 모듈

# 레이블이 잇는 윈도우를 생성해보자
# 하나의 레이블이 있는 윈도우를 생성

from tkinter import *   # ㅇtkinter 모듈을 포함

root = Tk()      # 루트 윈도우를 생성
root.geometry("500x200")       # WIdth x Height
label = Label(root, text="Hello tkinter")   # 레이블 위젯을 생성
label.pack()                # 레이블 위젯을 윈도우에 배치

root.mainloop()         # 윈도우가 사용자 동작을 대기

# -------------------------------------------------------------------


from tkinter import *

# 루트 윈도우를 생성
root = Tk()
root.title("tkinter 예제")
root.geometry("500x400")  # Width x Height

# 레이블 위젯을 생성하고 배치
label = Label(root, text="Hello tkinter")
label.pack(pady=10)

# 버튼 위젯을 생성하고 배치
def on_button_click():
    print("버튼이 클릭되었습니다!")
    label.config(text="버튼이 클릭되었습니다!")

button = Button(root, text="클릭하세요", command=on_button_click)
button.pack(pady=10)

# 입력 필드(Entry) 위젯을 생성하고 배치
entry_label = Label(root, text="이름을 입력하세요:")
entry_label.pack(pady=5)
entry = Entry(root)
entry.pack(pady=5)

# 체크박스 위젯을 생성하고 배치
checkbox_var = IntVar()
checkbox = Checkbutton(root, text="동의함", variable=checkbox_var)
checkbox.pack(pady=10)

# 라디오 버튼 위젯을 생성하고 배치
radio_var = StringVar()
radio_var.set("옵션1")

radio_label = Label(root, text="옵션을 선택하세요:")
radio_label.pack(pady=5)
radio1 = Radiobutton(root, text="옵션1", variable=radio_var, value="옵션1")
radio1.pack(pady=5)
radio2 = Radiobutton(root, text="옵션2", variable=radio_var, value="옵션2")
radio2.pack(pady=5)

# 리스트박스 위젯을 생성하고 배치
listbox_label = Label(root, text="항목을 선택하세요:")
listbox_label.pack(pady=5)
listbox = Listbox(root)
listbox.insert(1, "항목1")
listbox.insert(2, "항목2")
listbox.insert(3, "항목3")
listbox.pack(pady=10)

# 실행 버튼 위젯을 생성하고 배치
def on_submit():
    print(f"입력된 이름: {entry.get()}")
    print(f"체크박스 상태: {'동의함' if checkbox_var.get() else '동의하지 않음'}")
    print(f"선택된 옵션: {radio_var.get()}")
    selected_items = [listbox.get(i) for i in listbox.curselection()]
    print(f"선택된 항목: {selected_items}")

submit_button = Button(root, text="제출", command=on_submit)
submit_button.pack(pady=10)

# 윈도우가 사용자 동작을 대기
root.mainloop()

# Label: 텍스트를 표시하는 레이블.
# Button: 클릭 가능한 버튼.
# Entry: 텍스트를 입력할 수 있는 입력 필드.
# Checkbutton: 체크박스.
# Radiobutton: 라디오 버튼.
# Listbox: 여러 항목 중에서 선택할 수 있는 리스트박스.

# Label: 텍스트를 표시합니다.
# Button: 클릭 시 특정 동작을 수행합니다.
# Entry: 사용자로부터 텍스트 입력을 받습니다.
# Checkbutton: 체크할 수 있는 옵션을 제공합니다.
# Radiobutton: 여러 옵션 중 하나를 선택할 수 있습니다.
# Listbox: 여러 항목 중에서 하나 이상을 선택할 수 있습니다.

# 배치관리자
# 컨테이너 안에 존재하는 위젯의 크기와 위치를 자동적으로 관리하는 객체

# 배치 관리자의 종류
# pack: 압축 배치 관리자
# grid : 격자 배치 관리자
# place : 절대 위치 배치 관리자

# 파이썬 라이브러리
# 맷플롯립
# 몇 줄의 코드로 차트, 그래프, 파이 차트, 산점도, 히스토그램, 오류 차트 등을 그릴 수 있음