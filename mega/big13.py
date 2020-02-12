# 원래 가입한 아이디는 root임.
# 로그인할 id를 입력>> root
# 로그인 되었습니다.

#로그인 할 id를 입력>> root1
#로그인되지 않았습니다.


id1 = input("원래 가입한 아이디는")
print("로그인할 id를 입력>> " + str(id1))

if id1 == "root" :
    print('로그인 되었습니다.')
else :
    print("로그인되지 않았습니다.")