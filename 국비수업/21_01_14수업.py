# 객체지향은 
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
# 2. 클래스 메소드 선언
@classmethod #실행정보(annotation) @ 사용하여 클래스 메소드 선언

def get_plus_button(cls):
    return cls.button_name # 클래스(인스턴스간 공유) 변수

@classmethod #실행정보(annotation) @ 사용하여 클래스 메소드 선언
def set_plus_button(cls, op):
    return cls.button_name== op #클래스(인스턴스간 공유)변수

# FourCal()의 메소드를 호출하려면 FourCal의 인스턴스를 생성
cal1 = FourCal()
cal1.setdata(3,4)
print(cal1.mul())    

# 클래스 메소드 호출
# 클래스 이름. classmethod

FourCal.set_plus_button('+')
print(FourCal.get_plus_button())

print(cal1.get_plus_button())
print(cal2.get_plus_button())

# class FourCal:
#      button_name='--' #1. 클래스(인스턴스간 공유) 변수 선언
#      def setdata(self, first, second):
#          self.first = first #객체변수는 해당 인스턴스가 사유
#          self.second = second
#      def add(self):
#          result = self.first + self.second
#          return result
#      def mul(self):
#          result = self.first * self.second
#          return result
#      def sub(self):
#          result = self.first - self.second
#          return result
#      def div(self):
#          result = self.first / self.second
#          return result
#      #2. 클래스 메소드 선언
#      @classmethod #실행정보(annotation) @사용하여  클래스 메소드 선언
#      def get_plus_button(cls):
#          return cls.button_name #클래스(인스턴스간 공유) 변수
     
#      @classmethod #실행정보(annotation) @사용하여  클래스 메소드 선언
#      def set_plus_button(cls,op):
#          cls.button_name= op #클래스(인스턴스간 공유) 변수
# #FourCal의 메소드를 호출할려면 FourCal의 인스턴스를 생성 
# cal1 = FourCal()
# cal1.setdata(3, 4)
# print(cal1.mul())

# cal2 = FourCal()
# cal2.setdata(3, 4)
# print(cal1.add())
# #클래스 메소드 호출
# #클래스이름.classmethod
# FourCal.set_plus_button('+')
# print(FourCal.get_plus_button())


# 1. 사각형을 나타내는 클래스 Rectangle을 작성해보자. 
# Rectangle 클래스는 다음과 같은 변수와 메소드를 포함한다. 
# - 사각형의 폭과 높이를 나타내는 w와 h 
# - 사각형의 위치를 나타내는 x와 y 
# - 생성자 함수 및 각 변수의 세터,게터
# - 사각형의 넓이를 반환하는 calcArea()

# (1) 위와 같이 Rectangle 클래스를 정의한다.
# (2) 위치가 (0, 0)이고 크기가 (100, 100)인 Rectangle 객체를 생성한다. 
# 위치가 (10, 10)이고 크기가 (200, 200)인 Rectangle 객체를 생성 후 위치를 (20, 20)으로 수정한다.
# 각 사각형의 폭과 높이, 면적을 출력한다.
# 2. 동물를 나타내는 클래스 Animal이 다음과 같다.
# 고양이를 나타내는 클래스 Cat과 오리를  나타내는 클래스 Duck을 작성하여 보고
# Animal을 적절히 수정한다.(상속)
class Animal:
    def __init__(self, name):
        self.name = name 
    def move(self):
        pass
    def speak(self):
        pass

고양이
사뿐사뿐 이동한다
야옹 말한다
----------
오리
뒤뚱뒤뚱 이동한다
꽥꽥 말한다


class Rectangle:
    
    # def __init__(self,width,height,x,y):
    #      self.setdata(self,width,height,x,y)
        
    def setdata(self,width,height,x,y):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
      #넓이연산
    def calcArea(self):
        result = self.__width * self.__height
        return result
    
    #width 세터
    def set_width(self, width):
        #정제
        if width < 0 :
            self.__width = 0
        else:
            self.__width = width
            
    #height 세터
    def set_height(self, height):
        #정제
        if height < 0 :
            self.__height = 0
        else:
            self.__height = height
            
    #x 세터
    def set_x(self, x):
        #정제
        if x < 0 :
            self.__x = 0
        else:
            self.__x = x
            
    #y 세터
    def set_y(self, y):
        #정제
        if y < 0 :
            self.__y = 0
        else:
            self.__y = y
    def get_width(self):
            return self.__width
        def get_height(self):
            return self.__height
        def get_x(self):
            return self.__x
        def get_y(self):
            return self.__y


#%%

#initialize
sq=Rectangle()
sq.setdata(10,10,10,10)


#getting value
print(sq.get_width())
print(sq.get_height())
print(sq.get_x())
print(sq.get_y())
#area calc 
print(sq.calcArea())

#setting value
sq.set_width(5)
sq.set_height(10)
sq.set_x(12)
sq.set_y(7)
#getting value
print(sq.get_width())
print(sq.get_height())
print(sq.get_x())
print(sq.get_y())


class FourCal:
     #button_name='' #1. 클래스(인스턴스간 공유) 변수 선언
     #인스턴스마다 자신만의 객체 변수를 가진다(값이 다르다)
     def setdata(self, first, second):
         self.first = first #객체변수는 해당 인스턴스가 사유
         self.second = second
     def add(self):
         result = self.first + self.second
         return result

#%%
class Animal:
    def __init__(self, name):
        self.name = name 
    def move(self):
        pass
    def speak(self):
        pass

    
class Cat (Animal):
    
    def move(self):
        print("사뿐사뿐 이동한다")
    def speak(self):
        print("야옹 말한다")
 
class Duck (Animal):
    def move(self):
        print("뒤뚱뒤뚱 이동한다")
    def speak(self):
        print("꽥꽥 말한다")
cat = Cat("고양이")
print(cat.name)
cat.move()
cat.speak()
print('-'*10)
duck = Duck("오리")
print(duck.name)
duck.move()
duck.speak()

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