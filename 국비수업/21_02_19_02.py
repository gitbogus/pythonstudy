import numpy as np

lst = [
[1,2,3],
[4,5,6],
[7,8,9]
]

arr = np.array(lst) # 2차원 배열
ls = arr[0:2,0:1]
print(ls)

ls2 = arr[0:2,0] # array([1, 4])

ls3 = arr[0:2,0:]

ls4 = arr[:,:] # 모든배열

print(ls2)
print(ls3)
print(ls4)
