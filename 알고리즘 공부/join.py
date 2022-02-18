slayer = ["버피", "앤", "아스틴"]

a = " ".join(slayer)
print(a) # '버피 앤 아스틴'

b = "-<>-".join(slayer)
print(b) # 버피-<>-앤-<>-아스틴

c = "".join(slayer)
print(c) # 버피앤아스틴

d = "".join(reversed(slayer)) # 리버스를 함께 사용하기
print(d)
