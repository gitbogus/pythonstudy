# 다음 코드1를 읽고, 실행 결과를 알아맞혀 보세요.

number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)