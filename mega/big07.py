data = input("당신의 나이를 입력 ")
age = int(data)

#조건문(비교연산자)의 결과는 True/False 로 판단
if age >= 100 :# 콜론 =
    print('어른이시군요.!') #조건문의 결과가 참(True)
else :
    print("어른이 아니시군요.!") #조건문의 결과가 거짓(False)
# 나이가 100세 이상이면, 어른이시군요!
# 나이가 100세 미만이면, 어른이 아니시군요!
# 숫자로 변환할 필요가 있음.


# data는 ram의 저장공간을 말함.
# data의 저장공간을 변수라고 부른다.
# 변수들의 이름(=변수명)은 다 달라야 한다.
# 변수명은 소문자로 시작하는 것이 일반적이다.
# 변수명의 시작을 숫자로 시작하면 안된다.
# 파이썬에서는 변수명을 만들 때, 스네이크 표기법을 쓰는 것을 권장한다 EX) my_name, jiheon_cho
# 변수명은 한글, 일본어, 중국어를 사용 가능
# 유니코드를 지원
# 한글을 지양해야 함. (코딩은 전세계적으로 공유되어야 하기 때문에, 영어만을 원칙)