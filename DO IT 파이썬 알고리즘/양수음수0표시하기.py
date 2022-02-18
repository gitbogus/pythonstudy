# 입력받은 정수의 부호 (양수, 음수, 0)

n = int(input("정수를 입력하세요 : "))

if n > 0:
    print("{0}은 양수입니다".format(n))
elif n < 0 :
    print("{0}은 음수입니다.".format(n))
else:
    print("{0}은 0입니다.".format(n))

