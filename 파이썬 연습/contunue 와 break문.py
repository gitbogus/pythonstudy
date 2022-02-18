# 반복문 내에 쓸수 있는것
absent = [2, 5] # 결석
nobook = [7] #책을 깜빡햇네
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in nobook:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
