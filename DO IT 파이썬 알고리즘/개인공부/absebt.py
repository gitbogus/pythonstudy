absent = [2, 5] # 결석
for student in range(1, 11):
    if student in absent:
        continue
    print("{0}, 책을 읽어봐".format(student))
    


students = [1,2,3,4,5]
print(student)    
students = [i + 100 for i in students]
print(students)

from random import *
ride = 0 
customer = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        customer = customer + 1
        ride = ride + 1
        
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        customer = customer + 1
        continue
print("탑승한 인원은 총 {0}입니다.".format(ride))

