#2. 영어점수 입력: 76
#   수학점수 입력: 80
#   국어점수 입력: 60
#   ------------------
#   세 과목의 합은 216
#   세 과목의 평균은 72점


english = input("영어점수 입력: ")
math = input("수학점수 입력: ")
korean = input("국어점수 입력: ")
print("----------------------")

e = int(english)
m = int(math)
k = int(korean)

print("세 과목의 합은 " + str(e+m+k))
print("세 과목의 평균은 " + str(int((e+m+k)/3)))