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
