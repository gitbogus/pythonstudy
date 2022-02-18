# client
import socket
s = socket.socket()
s.connect(('127.0.0.1',3000)) # (인터넷 아이피주소, 포트정수번호)튜플
s.send('오늘의 메세지'.encode())
msg = s.conn.recv(1024) # 수신데이터 바이트배열(버퍼크기) print('수신데이터 바이트수',len(msg))
print('수신데이터 메세지', msg.decode())