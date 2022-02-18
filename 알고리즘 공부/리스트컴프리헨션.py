# 리스트컴프리헨션은 반복문의 표현식이다 (조건문을 포함할 수도 있다.)
# [ 항목 for 항목 in 반복 가능한 객체 ]
# [ 표현식 for 항목 in 반복 가능한 객체 ]
# [ 표현식 for 항목 in 반복 가능한 객체 if 조건문]

# 리스트 컴프리헨션의 좋은 예
result = []
for x in range(10):
    for y in range(5):
        if x * y > 10:
            result.append((x, y))

for x in range(5):
    for y in range(5):
        if x ! = y:
            for z in range(5):
                if y != z:
                    yield (x, y, z)

return ((x, complicated_transform(x)))
        for x in long_generator_function(parameter)
        if x is not None)

squares = [x * x for x in range(10)]

eat(jelly_bean for jelly_bean in jelly_beans)
    if jelly_bean.color == 'black')

# 리스트 컴프리헨션의 나쁜 예
result = [(x,y)] for x in range(10) for y in range(5) if x * y > 10]

return ((x, y, z)
        for x in xrange(5)
        for y in xrange(5)
        if x i = y
        for z in xrange(5)
        if y != z)