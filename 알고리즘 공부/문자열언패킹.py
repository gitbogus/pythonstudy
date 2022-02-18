# 문자열 언패킹 연산자는 **이며 이를 사용하면 함수로 전달하기에 적합한 키-값 딕셔너리가 생성된다.

hero = "버피"
number = "999"
a = "{number} : {hero}".format(**locals())
print(a)
print(type(a))