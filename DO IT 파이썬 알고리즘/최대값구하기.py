# 세정수를 받아 최대값 구하기

print("세 정수의 최대값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요. : "))
b = int(input("정수 b의 값을 입력하세요. : "))
c = int(input("정수 c의 값을 입력하세요. : "))


# maximum = a
# if b > maximum: maximum = b
# if c > maximum: maximum = c

# print(f'최대값은 {maximum}입니다.')

max = list(a,b,c)
for i in range(max)
    if a > b:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)

print("최대값은 {0} 입니다.".format(max))