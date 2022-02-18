#데이터 구조
#리펙토링
class Animal:
    def __init__(self, name,key):
        self.key=key
        self.name = name 
    def move(self):
        pass
    def speak(self):
        #print("말한다")
        return "말한다"
    #def displasy_animal_info(self):
    def __str__(self):
        # 변수를 문자열로 연결시 사이에 문자열 삽입
        return self.key+","+self.name+","+self.speak() 
    
#구체화,상세화,구현 
class Cat(Animal):
    def speak(self):
        #print("야옹 ",end='')
        return "야옹 "+ \
        super().speak()
 
class Duck (Animal):
    def speak(self):
        #print("꽥꽥 ",end='')
        return "꽥꽥 "+ \
        super().speak()
        
class Sparrow (Animal):
    def speak(self):
        #print("짹짹 ",end='')
        return "짹짹 "+ \
        super().speak()
        
        
#%%
def select_all():        
    for a in animal_list:
        print(a)        
#%%        
cat = Cat("고양이")
print(cat.name)
cat.move()   
cat.speak()
print('-'*10)

duck = Duck("오리") 
print(duck.name)
duck.move()   
duck.speak()
#%%
#저장소(주기억 장치) 리스트
animal_list=[]
#데이터 수집 
cat = Cat("고양이",'a1')
cat2 = Cat("고양이",'a2')
duck = Duck("오리",'a3')
sparrow = Sparrow("참새",'a4')
# 데이터 저장
animal_list.append(cat)
animal_list.append(cat2)
animal_list.append(duck)
animal_list.append(sparrow)

# 모든 동물들 말하기 조회
# 말하기 중복 제거
s=set()
for a in animal_list:    
    #print(a.speak())
    s.add(a.speak())
print(s)    
    
# 참새들 말하기 조건선택 조회
sel_bunho= \
input("동물이름(1) 동물키(2):")    
# 콘솔창 입력값은 문자
if sel_bunho=='1':
    aname=input("동물이름 : ")
    for a in animal_list:
        if a.name==aname:
            a.speak()    
else:
    akey=input("동물키 : ")
    for a in animal_list:
        if a.key==akey:
            a.speak() 

"새"in"참새" #True 
         
aname=input("동물이름일부 : ")
for a in animal_list:
    if aname in a.name:
        a.speak() 
           
aname=input("동물이름일부 : ")
for a in animal_list:
    if aname in a.name:
        print(a)

for a in animal_list:
    print(a)

#%% 수정(U)     
#'a1'is'a'
#a is b    
for a in animal_list:
    if a.key == 'a1':
        a.name='냥이'

#%% 삭제(D)
for a in animal_list:
    if a.key == 'a3':
        animal_list.remove(a)


#key :객체크기비교 기준변수
#리턴 함수               
sorted_animal_list=sorted(animal_list,
       key=lambda a:a.name,reverse=True) 

for a in sorted_animal_list:
    print(a)


#%%
f = open("animal.dat"    , 'w'   ,encoding='utf-8')
#다음 코드는 오류 write() argument must be str, not Cat
f.writelines(animal_list)
f.close()        
        
l=[]
for a in animal_list:
    l.append(a.__str__())

f.writelines(l)
f.close()
print('파일저장완료')
