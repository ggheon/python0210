# 네이버 로그인
# 판단을 할 때 조건을 가지고 판단을 한다.
# 조건이 하나가 아닌 경우 논리적으로 어떻게 판단하 것인가?
# 지하철을 타는 경우 1) 편해서 2)저렴해서
# 조건들이 모두 맞아야(All True) 논리적으로 판단
#   => and 조건(and), 파이썬은 쉽게 쉽게 가자라는 주의라 and 용법 그대씀 * 다른애들은 안그런애드도 있어
# 조건들 중에 하나만 맞아도(one True) 논리적으로 이렇게 맞아야 판단
#   => or 조건(or)
# 논리연산자

id = 'root'
pw = 'pass'

id2 = input('아이디 입력: ') #admin
pw2 = input('패스워드 입력: ') #1234

if (id == id2 and pw == pw2) :
    print('로그인 ok')
else :
    print('로그인 not')