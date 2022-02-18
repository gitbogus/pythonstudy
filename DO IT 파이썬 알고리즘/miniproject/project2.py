class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr


    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def load_contact(contact_list):
    f = open("C:/Users/sangmin/Desktop/git_practice/contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def contact_fix(contact_list):
    
    f = open("contact_db.txt", "rt")
    name = input("찾으시는 이름을 작성하세요 : ")
    phone_number = input("전화번호를 입력하세요 : ")
    new_name = input('수정할 이름을 입력하세요: ')
    new_call = input('수정할 전화번호를 입력하세요: ')
    for i in range(len(contact_list)) :
        if name or phone_number == contact_list[i]:
            contact_list[i].name=new_name
            contact_list[i].phone_number=new_call 
            print("변경 되었습니다!")
            break
    f.close()

def search(contact_list):
    import sys
    f = open("contact_db.txt", "rt")
    while True:
        name = input("검색할 이름을 입력하세요 [이전으로 돌아가기 : [Y] , 프로그램종료 : N]: ")
        if name == ('y' or 'Y'):
            print("이전으로 돌아갑니다.")
            break
        elif name == ('n' or 'N'):
            print('프로그램을 종료합니다.')
            sys.exit()
        for i in range(len(contact_list)):
            if (name == contact_list[i].name):
                print(contact_list[i].phone_number)
                break
            else: 
                print("검색한 이름이 없습니다.")
                break
        f.close()

def emailsearch(contact_list):
    import sys
    f = open("contact_db.txt", "rt")
    while True:
        email = input("검색할 이메일을 입력하세요 [이전으로 돌아가기 : [Y] , 프로그램종료 : N]: ")
        if email == ('y' or 'Y'):
            print("이전으로 돌아갑니다.")
            break
        elif email == ('n' or 'N'):
            print('프로그램을 종료합니다.')
            sys.exit()
        for i in range(len(contact_list)):
            if (email == contact_list[i].e_mail):
                print(contact_list[i].name)
                print(contact_list[i].phone_number)
                break
            else: 
                print("검색한 이메일이 없습니다.")
                break
        f.close()



def admin_print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 연락처 수정")
    print("5. 이름을 검색하여 연락처 찾기")
    print("6. email로 검색하기")
    print("7. 연락처 백업")
    print("8. 종료")
    # print("5. e-mail 검색")
    menu = input("메뉴선택: ")
    return int(menu)

def user_print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 이름을 검색하여 연락처 찾기")
    print("4. email로 검색하기")
    print("5. 연락처 백업")
    print("6. 종료")
    # print("5. e-mail 검색")
    menu = input("메뉴선택: ")
    return int(menu)

import random
def num_random():
    
    number1 = range(1000, 10000)
    number2 = range(1000, 10000)
    print("추천하는 번호는")
    cnt = 0
    while cnt < 5:
        random1 = (random.sample(number1, 1))
        random2 = (random.sample(number2, 1))
        cnt += 1
        print("[010]-{0}-{1}입니다.".format(random1, random2))
        if cnt >= 5:
            break

def run():
    import sys
    contact_list = []
    load_contact(contact_list)
    while True:
        mode = int(input("메뉴를 선택하십시오.\n 1. User / 2. Admin / 3. 프로그램 종료 4. 랜덤전화번호생성기 0. 프로그램 정보 : "))
        
        while True:
            if (mode == 1):
                while True:
                    # while 1:
                        menu = user_print_menu()
                        if menu == 1:
                            contact = set_contact()
                            contact_list.append(contact)
                            store_contact(contact_list)
                        elif menu == 2:
                            print_contact(contact_list)
                        elif menu == 3:
                            search(contact_list)
                        elif menu == 4:
                            emailsearch(contact_list)
                        elif menu == 5:
                            from project5 import __package__
                        elif menu == 6:
                            store_contact(contact_list)
                            sys.exit()
            elif (mode == 2):
                from project3 import __package__   # Admin일때 암호가 맞으면 허가 3번 틀리면 프로그램 종료 패키지
                
                menu = admin_print_menu()
                if menu == 1:
                    contact = set_contact()
                    contact_list.append(contact)
                    store_contact(contact_list)
                elif menu == 2:
                    print_contact(contact_list)
                elif menu == 3:
                    name = input("Name: ")
                    delete_contact(contact_list, name)
                elif menu == 4:
                    contact_fix(contact_list)
                elif menu == 5:
                   search(contact_list)
                
                elif menu == 6:
                    emailsearch(contact_list)

                elif menu == 7:
                    from project5 import __package__
                    
                elif menu == 8:
                    store_contact(contact_list)
                    sys.exit() 

            elif (mode == 3):
                
                answer = input("프로그램을 종료하시겠습니까? [Y] / [N] : ")
                if answer == ('y' or 'Y'):
                    print("프로그램을 종료합니다.")
                    sys.exit()
                elif answer == ('n' or 'N'):
                    print('메뉴로 돌아갑니다.')
                    break

            elif (mode == 4):
                num_random()
                answer = input("프로그램을 종료하시겠습니까? [Y] / [N] : ")
                if answer == ('y' or 'Y'):
                    print("프로그램을 종료합니다.")
                    sys.exit()
                elif answer == ('n' or 'N'):
                    print('메뉴로 돌아갑니다.')
                    break
                
            elif (mode == 0):
                print('''
                ____________________________________________________________
               | 프로그램명 : 전화번호부                                   | 
               | 만든이 : 노상민                                           | 
               | 참고 : wikidocs 파이썬으로 배우는 알고리즘 트레이딩       | 
               | 완성한 날짜 : 2021-01-21                                  | 
               |___________________________________________________________|  
                ''')
                answer = input("이전으로 돌아가시겠습니까 [Y] / [N] : ")
                if answer == ('y' or 'Y'):
                    print("이전으로 돌아갑니다.")
                    break
                elif answer == ('n' or 'N'):
                    print('프로그램을 종료합니다.')
                    sys.exit()
    
if __name__ == "__main__":
    run()




# 개선점 ex>검색기능 추가기능 상세보기 e-mail검색 백업기능 구조적 패키지 모듈 예외처리
# 소스코드 추가한 아이디어
