# 특정 클래스의 인스턴스 객체인지 아닌지를 확인하려면 어떻게 하는지를 설명해보시오.
# 이 문제는 어떤 클래스로 부터 만들어진 객체인지를 아는지에 대해서 묻는 문제이다.


# [1] : 클래스 생성
# 특정 클래스의 인스턴스 유무 확인 --> isinstance() 함수 사용 --> isinstance( 인스턴스 객체명, 클래스명 )
# ----------------------------
class Person:
        pass
        
class Monster:
        pass
# ----------------------------


# [2] : 클래스 사용
p1 = Person()
result = isinstance( p1, Person )  #--- p1 인스턴스 (객체)가 Person 클래스로 부터 만들어진거 맞냐? --> True or False --;;
print( '[1] p1 인스턴스는 Person 클래스의 인스턴스 객체가 맞나요? --> ', result )  #--- result 변수 안만들고 바로 print() 함수내에서 출력도 가능 --;;

result2 = isinstance( p1, Monster )
print( '[2] p1 인스턴스는 Monster 클래스의 인스턴스 객체가 맞나요? --> ', result2 )  #--- False















