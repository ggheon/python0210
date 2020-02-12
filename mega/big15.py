#이미 만들어 놓은 기능별 프로그램 단위 : 모듈(Module)
#패키지 -> 파일 -> 패키지 안에 세부기능별(모듈)로 만들어놓음.
#. = 접근연산자(안으로 들어감) like 'in'

#EX) 그래픽 프로그램은 그래픽 기능 from x import y
#EX) 크롤링 또한 동일.
#검색할시 python tkinter messagebox 에서 찾아볼것

from tkinter import messagebox

messagebox.showinfo("안녕하세요.", "홍길동이요.")
messagebox.showwarning("지금은 오후에요!", "졸음주의!")
result = messagebox.askquestion("시간체크", "지금은 오후인가요?", )
print(result)