a = [y for y in range(1900, 1940) if y%4 == 0]
print("a-", a)

b = [2 ** i for i in range(13)]
print("b-", b)

c = [str(round(355/113.0,i)) for i in range(1,6)]
print("c-", c)

words = 'Buffy is awesome and a vampire slayer'.split()
d = [[w.upper(), w.lower(), len(w)] for w in words]
for i in d:
    print("d-", i)