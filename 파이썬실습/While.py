num = 1
while num <= 100:
    print(num)
    num += 1
    

# input()으로 사용자로부터 정수를 한개 입력받아, 그 숫자를 숫자 크기만큼 반복해서
# 출력하는 파이썬 스크립트를 작성하세요.
# 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
# 단, while문을 사용하세요

a = int(input("숫자를 입력하면 그숫자만큼 반복되어 나옵니다. : "))

cnt = 0

while a:
    print(a)
    cnt += 1
    if cnt == a:
        break
    


num = int(input("숫자를 입력하면 그숫자만큼 반복되어 나옵니다. : "))

i = 0
while i < num:
    print('',num)
    i+=1
