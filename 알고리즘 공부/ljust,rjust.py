# A.ljust(width, fillchar) # 문자열 A '맨 처음'부터 문자열을 포함한 길이 width만큼 문자 fillchar를 채운다.
# A.rjust(width, fillchar) # 문자열 A '맨 끝'부터 문자열을 포함한 길이 width만큼 문자 fillchar를 채운다.

name = "스칼렛"
a = name.ljust(50, '-')
print(a)

b = name.rjust(50,'-')
print(b)