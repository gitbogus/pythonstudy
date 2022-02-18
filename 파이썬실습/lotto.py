from random import *

mylotto = []
num = 0
while True:
    for i in range(6):
        i = randrange(1,46)
    if i not in mylotto:
        num += 1
        mylotto.append(i)    
        print(f"{num}번째 숫자가 나왔습니다!! {i}입니다.")
        print("------------------")
    if len(mylotto) == 6:
        mylotto.sort()
        print("당신의 행운의 번호는!!")
        print(mylotto)
        break
    
        

        
        
