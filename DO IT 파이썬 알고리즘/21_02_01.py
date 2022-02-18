import socket
import random
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 3000))  # 인터넷 아이피 주소 문자, 포트 정수번호
#ss.bind(('',3000)) # 내컴퓨터의 모든 아이피를 바인드
ss.listen()
print("서버 시작")
while True:
    conn, addr = ss.accept() # 요청 수락 (송수신 통신 소켓,  클라이언트 주소)
    # print(addr, '서버연결완료')
    # conn
    msg = conn.recv(1024) # 수신 데이터 바이트 배열 (버퍼크기)
    print('수신데이터 바이트 수',len(msg))
    print('수신데이터 메세지',msg.decode()) # 수신데이터 문자열로 디코드

    open('index.html','r', )
    n = ['화이팅','잘해', '수고해']
    print(random.sample(n, 1))
    # n = conn.send('응답(송신)메세지 : 안녕'.encode()) # 송신데이터 바이트 배열로 인코드
    print('송신데이터 바이트 수(트래픽)' ,n)
    conn.close() # 소켓닫기 = 연결끊기



# import socket
# s= socket.socket()
# s.connect(('127.0.0.1',3002))#(인터넷아이피주소,포트정수번호)튜플 연결 요청(request)
# s.send('index.html'.encode())
# f= open('C:/Users/selene/Downloads/index.html','w',encoding='utf-8')
# while True:
#     msg = s.recv(1024)#수신데이터 바이트배열(버퍼크기) print('수신데이터 바이트 수',len(msg))
#     if not msg:
#         print('파일전송완료')
#         break
#     #print('수신데이터 메세지',msg.decode()) #수신데이터 문자열로 디코드
#     f.write(msg.decode()) #수신데이터 문자열로 디코드후 파일에 쓰기
    
# f.close()


# -*- coding: utf-8 -*-
# """
# Created on Tue Feb  2 10:33:05 2021

# @author: selene
# """
# import random

# def msg_choice():
#     l=['화이팅','잘해','수고해']
#     result= random.choice(l)
#     return result

# import socket
# ss= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ss.bind(('',3004))#내컴퓨터의 모든 아이피를 바인드
# ss.listen(5)#한번에 처리 가능한 클라이언트 수
# print("메신저 서버 시작")
# while True:#클라이언트 연결,데이터 전송요청 작업을 반복적으로 처리
#   try: 
#       conn,addr = ss.accept()#요청수락 (송수신 통신 소켓, 클라이언트 주소)
#       print(addr , '서버연결완료')
#       query = conn.recv(1024)#수신데이터 바이트배열(버퍼크기)  :block(수신대기) 
#       print('수신데이터 메세지',query.decode()) #수신데이터 문자열로 디코드
      
#       n= conn.send(msg_choice().encode())#송신데이터 바이트배열로 인코드 
#       conn.close()#소켓닫기 = 연결끊기
#   #클라이언트 콘솔창 강제 종료로 서버 정지(shutdown)
#   #ConnectionResetError: [WinError 10054] 현재 연결은 원격 호스트에 의해 강제로 끊겼습니다
#   except ConnectionResetError as e:
#       print('ConnectionResetError 발생', e)
# import socket
# s=socket.socket() #기본소켓
# s.connect(('localhost',3004))
# #이코드가 생략시 서버는 conn.recv(1024) 에서 블록(block)상태
# s.send("오늘의 메세지?".encode())#쿼리전송 
# while True:
#     msg = s.recv(1024)#수신데이터 바이트배열(버퍼크기) print('수신데이터 바이트 수',len(msg))
#     if not msg:       
#         break
#     print('수신된 오늘의 메세지 : ',msg.decode()) #수신데이터 문자열로 디코드
# s.close()
