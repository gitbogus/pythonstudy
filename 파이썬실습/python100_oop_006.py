# 이름과 나이를 전달받아 객체를 생성하는 Person 클래스를 만들고 객체 정보를 출력하시오.
# 정보를 생성하는 메서드명 --> create_info()
# 정보를 출력하는 메서드명 --> print_info()


# [1] : 클래스 생성
print( '[ 클래스를 사용한 캐릭터 생성 및 정보 출력 ]' )
# --------------------------------------------
class Person:
        
        # 정보 생성
        def create_info( self, name, age ):
                self.name = name
                self.age = age
                
        # 정보 출력
        def print_info( self ):
                print( '-' * 33 )
                print( 'Name : ', self.name )
                print( 'Age : ', self.age )
                # print( '-' * 33 )
# --------------------------------------------


# [2] : 클래스 사용
p1 = Person()
p1.create_info( '홍길동', 20  )
p1.print_info()

p2 = Person()
p2.create_info( '강감찬', 40 )
p2.print_info()

p3 = Person()
p3.create_info( '을지문덕', 30 )
p3.print_info()
























