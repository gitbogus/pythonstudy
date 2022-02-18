dinner= ['a', 'b', 'c']


dinner.insert(2,'유재석')
print(dinner)
dinner.append('조세호')
print(dinner)

# for i in dinner:
#     print(f'{i}님 저녁식사에 초대되셨어요!')

# for i in range(1,4):
#     remove_list = dinner.pop(-1)
#     print(remove_list)

for i in dinner:
if list[len(i)] == 2:
    print("자리는 두분만 참석 가능합니다.")