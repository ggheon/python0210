#교보문고에 가서 1000원짜리 스티커 3장과
#2500원짜리 책갈피를 4개 샀습니다.
#우수회원 할인으로 10%할인을 받았습니다.
#내가 낸 금액은 얼마일까요?


sticker = input("스티커")
booklet = input("책갈피")
sticker_count = input("스티커 개수")
booklet_count = input("부클릿 개수")
#
s = int(sticker)
b = int(booklet)
s_c = int(sticker_count)
b_c = int(booklet_count)
w = "우수회원"

if w == "우수회원":
    print((s*s_c + b*b_c)- ((s*s_c+ b*b_c)/10))
else:
    print(s*s_c + b*b_c)