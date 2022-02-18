# 사용자로부터 생년월일을 받아서 올바른 생년월일인지를 검사하여 
# 올바른 생년월일이면 datetime 객체로 생성하여 다음 형식으로 출력하는 프로그램을 작성하라. 

# 제약조건은 월은 1 에서 12 , 일은 1 에서 31
# 예를 들면 “19951301”과 같은 문자열은 올바른 생년월일이 아니다. 13월 1일은 올바르지 않다. 

# 생년월일을을 입력하시오: 20210122
# 생년월일 : 2021-01-22  오후 05:21


import time
while 1:
    birthdate = print(input("생년월일을 입력하세요 : "))
    if not birthdate: break
    year = int(birthdate[:4])
    month = int(birthdate[4:6])
    day = int(birthdate[6:])
    thisyear = int(time.strftime('%Y'))
    print('%s년 %s월 %s일 생'%(year,month,day))
    print('%d살'%(thisyear-year))


