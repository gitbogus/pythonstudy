ps = "0000"
cnt = 0
while cnt < 3:
    cnt += 1
    password = input("암호를 입력하세요 : ")
    if password == ps:
        print("환영합니다 관리자님!")
        break
                        
    else:
        print("암호가 틀립니다")
    if cnt >= 3:
        print("암호가 3번 연속 틀렸습니다. 프로그램을 종료합니다.")
        exit()