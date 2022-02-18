# class Mother:
#     def m(self):
#         print("난 엄마")

# class Father(Mother):
#     #m()
#     def f(self):    
#         print("난 아빠")

# class Me(Father):    
#     def showme(self):
#         super().m() 
#         super().f()        
#         print("난 자식")

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 80, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)




# people = print(input("승차인원은 몇명인가요 : "))

# class tada:
#     def setdata(self , people , bus, taxi):
#         self.__people = people
#         self.__bus = bus
#         self.__taxi = taxi
        
#     def set_people(self, people):
#         if people < 0 :
#             self.__people = 0
#         else:
#             self.__people = people
    
#     def set_bus(self, bus):
#         print(f'{people}' * 100 )
    
#     def set_taxi(self,taxi):
#         if super().p() <= 5:
#             print("기본요금 입니다."))
#         else:
#             print(f'{taxi}'*100 + 1000)

# print(10,10,10)

# class tada:
#     def __init__(self, people, taxi):
#         self.people = people
#         self.taxi = taxi
        
#         print("{0} 명의 손님이 타셨습니다.".format(self.people))
    
    
#         if self.people() <= 5:
#             print("기본요금 입니다.")
#         else:
#             print(f'{self.people}'* 100)

# coco = tada(10)


# 대중교통 과금 시스템

# 버스 택시
# 공통기능 : 승차하다,과금하다

# 버스 : 승차인원수 * 100
# 택시 : 거리(KM) * 100 + 기본료(1000)
# 택시 : 거리(KM) * 100 + 기본료(1000)
# 기본 구간은 5KM 기본료과금

class Car:
    def __init__(self,fee):# fee 요금 (택시이면 500, 버스이면 0으로 초기화)
        self.fee=fee
    def ride(self):
        print("승차")
    def pay(self,d):
        pass
    def getfee(self):
        return self.fee
    #def set_fee(self, fee)
    #   self.fee = fee

class Taxi(Car):
    def pay(self,d):#d가 거리 7
        if d > 5:  # 2km당 100원
            self.fee = self.fee+((d-5 / 2) * 100) # 기본요금 + 추가요금 = 700

class Bus(Car):
    def pay(self, d): #d 인원수 7 
        self.fee = self.fee+(d *100) # 기본요금 + 추가요금 = 700


def main():
    t = Taxi(500)
    d = int(input("주행거리(km) : "))
    t.ride()
    t.pay(d)
    print("요금(원) = ", t.getfee())

    t = Bus(0, False) # 현금결제
    d = int(input("승차인원수 : "))
    t.ride()
    t.pay(d)
    print ("요금(원) = " , t.getfee())


main()


