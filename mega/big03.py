#컴퓨터가 생각하는 데이터의 타입
#컴퓨터는 모든 입력을 문자로 인식한다.
#문자로 인식하는 데이터를 어떤 타입으로 쓸지 프로그래머가 결정한다.
#python 은 타입이 일치해야 출력이 된다.
#java는 하나라도 문자면 문자로 취급해서 출력함
#str = string(문자), int = integer (정수)
#괄호 ----------
# () 소괄호 -> 명령어의 입력값 지정
# {} 중괄호 -> 포함(묶어준다는 의미)
# [] 대괄호 ->

number1 = input("나이 입력>> ") #100:문자로 인식

#int(정수, integer) 로 변환 처리

age = int(number1) #명령어(입력값) #100:숫자로 인식(정수=소수점이 없는 숫자, 실수=소수점이 있는 숫자)

print("내년 나이는 ", age + 1 )

#컨트롤+쉬프트+F10 = 해당 파일 실행
