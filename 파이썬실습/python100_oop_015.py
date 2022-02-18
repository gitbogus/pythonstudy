# 클래스의 인스턴스 객체가 생성될 때 마다 객체의 카운트를 1씩 증가시키는 클래스를 구현하시오.
# 이때 카운트 증가 함수는 클래스내 메서드를 통해서 구현한다.


# [1] : 클래스 생성
# ------------------------------------
class Person:
        
        # 클래스 변수
        count_class_var = 0
        
        # 생성자
        def __init__( self, name, age, power ):
                self.name = name
                self.age = age
                self.power = power
                self.increase_obj()

        # 클래스 메서드
        def increase_obj( self ):
                Person.count_class_var += 1
# ------------------------------------


# [2] : 클래스 사용
print( '현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var )  #--- 0

p1 = Person( '홍길동', 20, 9 )
print( '현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var )  #--- 1

p2 = Person( '강감찬', 30, 8 )
print( '현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var )  #--- 2

p3 = Person( '을지문덕', 40, 7 )
print( '현재까지 생성된 인스턴스 객체의 갯수 --> ', Person.count_class_var )  #--- 3


















































