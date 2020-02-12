print("----------------")
#data1은 커피값 입력 변수
data1 = input("커피값 입력: ")
#data2는 커피 인원수 변수
data2 = input("커피 인원수: ")
# print("힌트 : sum = price * count")
#data1에 입력된 변수 값을 정수로 선언
price = int(data1)
#data2에 이벽된 변수 값을 정수로 선언
count = int(data2)
#data3은 price 와 count 의 곱을 입력하는 변수
data3 = price * count
#sum 은 정수 값 data3 을 입력하는 변수
sum = int(data3)

#만약, sum 이 20000원 이상이면, "2000원을 할인해드립니다." 라는 내용을 출력

if sum >= 20000 :
    print("2000원을 할인해드립니다.")
#sum이 20000원 이상을 넘지 않는다면, "계산값을 다 지불하셔야 합니다" 라는 내용을 출력
else :
    sum < 20000
    print("계산값을 다 지불하셔야 합니다.")
