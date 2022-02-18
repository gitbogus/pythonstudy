import time
import threading

def sum(low, high):
    total = 0
    for i in range(low, high):
        time.sleep(0.1)
        total += i
        print(total)
    print("Subthread", total)

# sum 이라는 함수를 쓰레드가 실행하도록 threading.Thread()함수의 파라미터로
# target = sum 을 지정
# sum() 함수는 두 개의 파라미터를 받아들이기 때문에 "args=(1, 100000)" 와 같이
# 입력파라미터를 지정
t = threading.Thread(target=sum, args=(1,100))
t.start()
t2 = threading.Thread(target=sum, args=(1,100))
t2.start()

print("Main Thread")
print("Main Thread")
print("Main Thread")
