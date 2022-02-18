try:
    f= open('test.txt','r',encoding='utf-8')    
except FileNotFoundError:
    #pass
    #open('test.txt','w',encoding='utf-8') 
    #재시도 (retry)
    with open('test.txt','r',encoding='utf-8') as f:
        f.read()

f.close()

       
#%%
import sys
for i in range(3): # ValueError 3번 반복 
    try:    
        a = int(input( '정수>>')) #B 입력시 ValueError
        print(a)        
        
    except Exception as e:
        print(e)
        if(i==2) :
            print('정수아니다.너 사람아니지..!')
            #raise Exception('정수아니다') #Exception: 정수아니다
            sys.exit() 
    else:
        break
    
print('다음 코드')

#숫자 여부
s ='1.2'
def isNumber(s):
    try:
        a,b=s.split(".")
        print(a,b)
        float(s)
        return True
    except ValueError:
        return False

su=None    
if isNumber(s):
    if '.' in s:#실수
        su=float(s)
    else:#정수
        su=int(s)
print(su)
