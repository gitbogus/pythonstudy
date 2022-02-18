import collections
Person = collections.namedtuple('Person', 'name age gender')
# person = collections.namedtuple('Person',['name','age','gender])
# person = collections.namedtuple('Person',('name','age','gender'))
p = Person('아스틴', 30, '남자')
print(p[0])

print(p.name)

# print(p.age)=20
