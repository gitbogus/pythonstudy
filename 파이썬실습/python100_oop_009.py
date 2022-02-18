# 생성자를 이용하여 객체를 생성하는 코드이다. 결과로 출력되는 것을 말해보시오.
# 결과가 다르게 나온다면 이유를 설명해보시오.


# [1] : 클래스 생성
# -----------------------------------------
class SmartPhone:

        # 생성자
        def __init__( self, name, price ):
                self.name = name
                self.price = price
                print( self.name + " 스마트폰 객체가 생성되었습니다." ) 
                print( '-' * 40 )
                print( self.name + " 스마트폰의 가격은 " + str(price) + "원 입니다." ) 
                print( '-' * 40 )
# -----------------------------------------


# [2] : 클래스 사용
s1 = SmartPhone( '엘지', 500000 )






















