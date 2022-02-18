import numpy as np
lst = [1, 2, 3]  # 1차원 리스트

arr = np.array(lst)
print(arr)
print(arr.ndim) # 차원수
print(arr.shape) # 배열구조 (크기)
print(arr.size) #배열요소개수
print(arr.dtype) # 요소 자료형 int32

# 배열 감안하여 리스트 고정된 동일 요소자료형 권장
# 2차원 리스트
# lst = [
# [1,2,3,4],
# [4,5,6,7]
# ]
lst = [
[1,2,3],
[4,5,6]
]

# arr = np.array(lst) # 2차원 배열
# arr = np.array(lst,dtype=float) # 2차원 배열
arr = np.array(lst,dtype=np.float64) # 2차원 배열
print("1 - ", arr)
print("2 - ", len(arr)) # 배열요소 개수
print("3 - ", arr.ndim) # 차원수
print("4 - ", arr.shape) # 배열구조(크기)
print("5 - ", arr.size) # 배열요소 개수
print("6 - ", arr.dtype) # 요소자료형 int32

arr[0,0]
arr[1,0]
arr[1,2]