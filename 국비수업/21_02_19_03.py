# 확장 배열슬라이싱
import numpy as np


lst = [
[1,2,3],
[4,5,6],
[7,8,9]
]

arr = np.array(lst) # 2차원 배열
ls = arr[0:3:2, 0:3:2] # 행 시작인덱스 : 행끝 인덱스 : 이동증감값
print(ls)

ls2 = arr[0:3:,::2]
print(ls2)