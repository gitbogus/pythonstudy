import numpy as np

# 배열 불린 인덱싱
# 인덱스 번호대신 논리형 인덱스 배열을 지정
# 논리형 인덱스 배열을 조건식으로 생성

lst = [
[1,2,3],
[4,5,6],
[7,8,9]
]

arr = np.array(lst) # 2차원 배열
# 짝수만 뽑아내는 부울린 인덱싱 배열 ( numpy 배열 )
ls = arr[arr % 2 == 0]
ls1 = arr[0:3:, ::2]
ls2 = arr[arr > 3]
print(ls)
print(ls1)
print(ls2)