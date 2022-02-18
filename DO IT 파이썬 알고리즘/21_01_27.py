import re

data = "python is good!"

p=re.compile("[a-z]+")
m=p.findall(data)
print(m)
# [출처] [Day14] 파이썬 정규표현식은 머지? - 메서드 findall|작성자 컴맹