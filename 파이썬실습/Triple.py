# def triple(x):
#     a = x * 3
#     return a

# print(triple(3))
# print(triple("'x'"))

from datetime import datetime
# today = datetime.today()
# print(today)
# datetime.datetime(2021, 3, 21, 15, 46, 1, 94942)
# print(today.year)

def korean_age(c):
    today = datetime.today()
    a = today.year
    b = a - c
    return b

c = int(input("태어난 날짜를 입력하면 나이가 나옵니다 : "))
print(korean_age(c))