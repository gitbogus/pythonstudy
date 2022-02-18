import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: '파이썬'}
data2 = [1, 2, 3]
pickle.dump(data,f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
f.close()
print(data)

for k,v in data.items():
     print(k,v)

for v in data2:
    print(v)

# 다중객체를 한꺼번에 묶음 저장
# collect_data = [data, data2]
# pickle.dump(collect_data, f) # 이진 파일 복호화

#다중 객체를 따로 따로 저장
pickle.dump(data, f)
pickle.dump(data2,f)
f.close

import os
os.environ['PATH']

os.getcwd()
os.path.exists #(c/)
os.mkdir() # 디렉토리 만드는 명령어 # os.mkdir('c:/pytest')
f = open('text.txt','w',encoding='utf-8')
f.close()
os.rmdir() # 디렉토리 삭제하는 명령어
# os.unlink('c~~) = os.remove('c~~)

# 경로를 입력받은 후 
# 경로가 디렉터리이면 경로뒤에 (d)를 붙이고 
# 경로가 파일이면 경로뒤에 (f)를 붙여서 파이썬 리스트로 반환

# path="d:/pytest"

# (lambda path:[x+'(d)' 
#  for x in os.listdir(path) if os.path.isdir(path+'/'+x) ])(path)

# (lamda path:[x+'(d)' if os.path.isdir(path+'/'+x)
# else x+'(d)' for x in os.listdir(path) ]) (path)

import tempfile
filename = tempfile.mkstemp()
filename

import time
time.time()

time.strftime("%Y%m%d%H%M%S", time.localtime())



#%%
#실행시간 프로파일링
import time
stime=time.time()
for x in range(0,10000):
    print(x)
etime=time.time()
print(f'실행시간={etime-stime}')


