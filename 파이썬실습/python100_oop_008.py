# 이름과 나이를 전달받아 객체를 생성하는 Person 클래스를 만들고 객체 정보를 출력하시오.
# 파이썬 클래스의 생성자 메서드를 사용해서 구현하시오.
# 아래 예제는 앞서 다루었던 예제를 생성자 메서드를 사용해서 똑같이 구현할 수 있는지를 묻는 문제이다.


# [1] : 클래스 생성
print( '[ 클래스를 사용한 캐릭터 생성 및 정보 출력 ]' )
# --------------------------------------------
class Person:
        
        # 생성자
        def __init__( self, name, age ):
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
# __init__ 메서드 사용 --> X
# p1 = Person()
# p1.create_info( '홍길동', 20 )
# p1.print_info()

# __init__ 메서드 사용 --> O
p1 = Person( '홍길동', 20 )
p1.print_info()

p2 = Person( '강감찬', 30 )
p2.print_info()

p3 = Person( '을지문덕', 40 )
p3.print_info()

























