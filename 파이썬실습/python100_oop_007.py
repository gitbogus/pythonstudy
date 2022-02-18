# 파이썬 클래스에서 생성자 메서드란 무엇인지 설명해보시오.
# 아래 클래스를 사용해서 "객체가 하나 생성되었습니다."를 화면에 출력해보시오.
# 자바와 같은 OOP 언어하고 다르게 구현이 되어지는 파이썬 클래스의 생성자 메서드에 대해서 아는지를 묻는 문제이다.


# [1] : 클래스 생성
# ------------------------------------------
class Person:
        # 생성자
        def __init__( self ):
                print( '객체가 하나 생성되었습니다.' )
# ------------------------------------------


# [2] : 클래스 사용
# Person() 클래스내에 내가 만든 메서드(함수)가 한개도 없지만 객체를 생성하는 순간 생성자 메서드는 제일 먼저 자동 호출.
p1 = Person()


# [ ! ] : __init__ 생성자 메서드란?
# 생성자 메서드를 통해서 객체가 생성될 때 해당 객체의 여러 초기 값을 셋팅할 수 있다.
# 다양한 객체를 생성해낼 때 이 생성자를 이용하며, 각 객체의 초기 값들을 설정하면서 여러 객체들을 만들어낸다.
# 생성자나 소멸자와 같이 앞뒤에 '__' 2개가 붙은 경우에는 특별한 용도로 사용되는 메서드라는 뜻이다.
# 그래서 '스페셜 메서드'라고도 부른다.










