# client
import socket
s = socket.socket()
s.connect(('127.0.0.1',3000)) # (인터넷 아이피주소, 포트정수번호)튜플
s.send('Hi'.encode())
while True:
    msg = s.recv(1024) # 수신데이터 바이트 배열 (버퍼크기) print('수신데이터 바이트 수',len(msg))
    if not msg:
        break
    print('수신데이터 메세지', msg.decode()) # 수신데이터 문자열로 디코드
    