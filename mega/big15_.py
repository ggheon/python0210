#while 반복문
#python 에서 True의 T는 대문자

#한 줄 주석처리는 Ctrl + / : 자동주석이다.

# while True :
#     print('1시간 남았어요.')

# a = 10
# while a > 0 :
#     print(a)
#     a = a - 1

# 1. 0부터 100까지 찍어보세요.

# while b < 100 :
#     print(b + 1)
#     b = b + 1

#2. 1부터 100까지 찍어보세요.

# b = 1
# while b < 101 :
#     print(b, end= ' ')
#     b = b + 1

# #3. 1부터 100까지 중 짝수만 찍어보세요.
# b = 1
# while b < 100:
#     if ( b % 2 == 0) :
#         print(b)
#     b = b + 1

#4. 0~99 중 3의 배수를 찍어보세요.

# c = 0
# while c < 100 :
#     if ( c % 3 == 0 ) :
#         print(c)
#     c = c + 1

#5. 0~99 중 5의 배수의 개수를 구해보세요. (같이풀기)

start = 0
count = 0
while start < 100 :
    if start % 5 == 0 :
        count = count + 1 # 5의 배수일때만 증가시키는 애
    start = start + 1 #0부터 99까지 돌리는 애
print('5의 배수는', count, '개')


# d = 0
# while d < 100 :
#     if ( d % 5 == 0) :
#         print(d)
#     d = d + 1

#6. 안녕히가세요 5번 프린트 (같이풀기)

# h = 1
# while h < 6 :
#     if ( h < 6) :
#         print("안녕히가세요")
#     h = h + 1

# start = 0 # 시작
# while start < 5 :  #조건
#     print('안녕히가세요.')
#     start = start + 1 #증감식

# a = 100
# print(a)
