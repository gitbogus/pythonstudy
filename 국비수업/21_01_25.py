from datetime import datetime

b = input("생년월일을 입력: ")
year = int(b[:4])
month = int(b[4:6])
day = int(b[6:])
# 올바른 생년월일인지를 검사
if month > 0 and month <13:
    if day > 0 and day < 32:
        #datetime 객체로 생성하여 다음 형식으로 출력
        bd = datetime(year,month,day)
        bstring = datetime.strftime(bd, "%Y-%m-%d %a %p %I:%m")
        bstring.replace('AM', '오전').replace('PM','오후')
        print(bstring)
    else:
        print("올바르지 않은 생년월일입니다.")
else:
    print("올바르지 않은 생년월일 입니다.")

    