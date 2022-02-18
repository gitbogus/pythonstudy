# 파이썬 클래스에서 소멸자란 무엇인지 설명해보시오.
# 클래스내에서 생성자와 소멸자를 모두 구현한 예제를 하나 만들어보시오.


# [1] : 클래스 생성 --> 생성자, 소멸자
# 생성자는 객체가 생성될 때 실행되고, 소멸자는 객체가 소멸될 때 실행된다.
# 생성자는 __init__ 속성을 사용하고, 소멸자는 __del__ 속성을 사용해서 정의한다.
# --------------------------------------------------------------
class SmartPhone:
        
        # 생성자
        def __init__( self, name, price ):
                self.name = name
                self.price = price
                print( self.name + " 스마트폰 객체가 생성되었습니다." )
                print( '-' * 40 )
                print( self.name + " 스마트폰의 가격은 " + str(price) + "원 입니다." )
                print( '-' * 40 )

        def a_method( self ):
                print( 'a_method가 호출되었습니다.' )

        # 소멸자
        def __del__( self ):
                print( self.name + " 스마트폰 객체가 소멸되었습니다." )
# --------------------------------------------------------------


# [2] : 클래스 사용
s1 = SmartPhone( '엘지', 500000 )
s1.a_method()
# del s1

s1.a_method()













































