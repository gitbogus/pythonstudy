try:
    4 / 0
except ZeroDivisionError as e:
    print("예외", e)
else: # 예외미발생시
    print("예외미발생")
print("프로그램 종료")

try:
    f = open('bar'.txt, 'r')
except FileNotFoundError:
    pass
finally:
    f.close()
print("프로그램 정상종료")