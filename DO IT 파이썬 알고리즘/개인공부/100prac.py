# # 소인수 분해

# n = int(input())
# li = []
# i = 2

# while n > 1:
#     if n % i == 0:
#         li.append()
#         n = n//i
#     else:
#         i = i + 1

# for i in range(len(li)-1):
#     print(li[i],end=' ')

# print(li[len(li)-1]) 

# 리스트 컴프리헨션
# a = [y for y in range(1900,1940) if y%4 == 0]
# print (a)
# b = [2**i for i in range(13)]
# print(b)
# c = [x for x in a if x%2==0]
# print(c)
# d = [str(round(355/113.0, i))for i in range(1, 6)]
# print(d)
# words = 'Buffy is awesome and a vampire slayer'.split()
# e = [[w.upper(),w.lower(),len(w)] for w in words]
# for i in e:
#     print(i)

# 딕셔너리
tarantino = {}
tarantino['name'] = '쿠엔틴 타란티노'
tarantino['job'] = '감독'
print(tarantino)

sunnydale = dict({"name":"버피", "age":16, "hobby":"게임"})
print(sunnydale)

# setdata
def usual_dict(dict_data):
    """dict[key] 사용"""
    newdata = {}
    for k, v in dict_data:
        if k in dict_data:
            if k in newdata:
                newdata[k].append(v)
        else:
            newdata[k]=[v]
    return newdata

def setdefault_dict(dict_data):
    """setdefault() 메서드 사용 """
    newdata = {}
    for k, v in dict_data:
        newdata.setdefault(k, []).append(v)
    return newdata

def test_setdef():
    dict_data = (("key1", "value1"),
                 ("key1", "value2"),
                 ("key2", "value3"),
                 ("key2", "value4"),
                 ("key2", "value5"),)
    print(usual_dict(dict_data))
    print(setdefault_dict(dict_data))

if __name__ == '__main__':
    test_setdef()
