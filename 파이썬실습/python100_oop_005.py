# 아래 코드의 결과로 출력되는 것을 말해보시오.
# 이 문제는 클래스 사용법과 클래스내 메서드 작성법에 대해서 아는지를 묻는 문제이다.


# [1] : 클래스 생성
# ----------------------------------------
class Pet:
        # 짖다
        def bark_dog(self):
                print( '멍멍~' )
        def bark_cat(self):
                print( '야옹~야옹~' )
        def bark_hamster(self):
                print( '찍찍~' )
# ----------------------------------------


# [2] : 클래스 사용
p1 = Pet()
p1.bark_dog()

p2 = Pet()
p2.bark_cat()
p2.bark_dog()

p3 = Pet()
p3.bark_hamster()











