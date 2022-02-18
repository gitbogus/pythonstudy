import numpy as np

print(np.arange(0, 30, 2))

print(np.random.random((3,3)))

nptype = np.ones((3,3), dtype = bool)
print(nptype)

date = np.array('2020-01-01', dtype = np.datetime64)
print(date)

plus = date + np.arange(12)
print(plus)

# def array_info(array):
#     print(array)
#     print("ndim:", array.ndim)
#     print("shape:", array.shape)
#     print("dtype:", array.dtype)
#     print("size:", array.size)
#     print("itemsize:", array.itemsize)
#     print("nbytes", array.nbytes)
#     print("strides:", array.strides)

# a1 = [4,5,6,4,5]
# print(array_info(a1))

a2 = np.array([[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]])
print(a2)
print(a2[1][1])
print(a2[1][2])

a1 = np.array([4, 5, 6, 4, 5]) 
print(a1)
b1 = np.insert(a1, 0, 10)
print(b1)
c1 = np.insert(a1, 2, 10)
print(c1)

print(a2)
a2[0, 0] = 1
a2[1, 1] = 2
a2[2, 2] = 3
a2[0] = 1
print(a2)

print(a1)
b1 = np.delete(a1, 1)
print(b1)
print(a1)

print(a2)
b2 = np.delete(a2, 1, axis = 0)
print(b2)

# 슬라이싱 값변환
print(a2)
print(a2[:2, :2])
a2_sub = a2[:2, :2]
print(a2_sub)
a2_sub[:, 1]=0
print(a2_sub)
print(a2)


# copy
print(a2)
a2_sub_copy = a2[:2, :2].copy()
print(a2_sub_copy)
a2_sub_copy[:, 1] = 1
print(a2_sub_copy)
print(a2)

# 배열 전치 및 축 변경
print(a2)
print(a2.T)

# 배열 재 구조화
n1 = np.arange(1, 10)
print(n1)
print(n1.reshape(3, 3))

# 새로운 축 추가 newaxis
print(n1)
print(n1[np.newaxis, :5])
print(n1[:5, np.newaxis])

# 배열 모양만 변경
n2 = np.random.randint(0, 10, (2, 5))
print(n2)
n2.resize((5,2))
print(n2)

# 배열 크기 증가
n2.resize(5, 5)
print(n2)

# 배열 추가
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2 = np.arange(10, 19).reshape(3, 3)
print(b2)

c2 = np.append(a2, b2, axis=0)
print(c2)


c2 = np.append(a2, b2, axis=1)
print(c2)


# 배열 연결
# concatenate() : 튜플이나 배열의 리스트를 인수로 사용해 배열 연결

a1 = np.array([1, 3, 5])
b1 = np.array([2, 4, 6])
np.concatenate([a1, b1])

c1 = np.array([7, 8 ,9])
np.concatenate([a1, b1, c1])

# vstack : 수직 스택() 1차원으로 연결

np.vstack([a2, a2])

# hstack() : 수평 스택 (horizontal stack), 2차원 연결
np.hstack([a2, a2])

# dstack() : depth stack 3차원 연결
np.dstack([a2, a2])

# 새로운 차원으로 연결
np.stack([a2, a2])

# 배열 분할
# split()
a1 = np.arange(0, 10)
print(a1)
b1, c1 = np.split(a1, [5])
print(b1, c1)

b1, c1, d1, e1 ,f1 = np.split(a1, [2, 4, 6, 8])
print(b1, c1, d1, e1, f1)

# vsplit () : 수직 분할 1차원으로 분할
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2, c2 = np.vsplit(a2, [2])
print(b2)
print(c2)

# hsplit() : 수평분할, 2차원으로 분할
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2, c2 = np.hsplit(a2, [2])
print(b2)
print(c2)

# dsplit() : 깊이 분할, 3차원으로 분할
a3 = np.arange(1, 28).reshape(3, 3, 3)
print(a3)
b3, c3 = np.dsplit(a3, [2])
print(b3)
print(c3)

# 배열 연산

a1 = np.array([1, 2, 3])
print(a1)
print(a1 + 5)

a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print(a1 + a2)

b2 = np.array([1, 2, 3]).reshape(3, 1)
print(b2)
print(a1 + b2)

# 산술 연산
a1 = np.arange(1, 10)
print(a1)
print(a1 + 1)
print(np.add(a1, 10))
print(a1 - 2)
print(np.subtract(a1, 10))
print(-a1)
print(np.negative(a1))
print(a1 * 2)
print(np.multiply(a1, 2))
print(a1 / 2)
print(np.divide(a1, 2))
print(a1 // 2)
print(np.floor_divide(a1 , 2)) # 내림으로 바꿔줌
print(np.power(a1, 2))
print(a1 ** 2)
print(a1 % 2)
print(np.mod(a1, 2))


a1 = np.arange(1, 10)
print(a1)
b1 = np.random.randint(1, 10, size = 9)
print(b1)
print(a1 + b1)
print(a1 - b1)
print(a1 * b1)
print(a1 / b1)
print(a1 // b1)
print(a1 * b1)
print(a1 % b1)

# 함수

t = np.linspace(0, np.pi,3 )
print(t)
print(np.sin(t))
print(np.cos(t))
print(np.tan(t))

# 집계 함수
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
