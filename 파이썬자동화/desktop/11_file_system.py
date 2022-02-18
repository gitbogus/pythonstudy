# 파일 기본
import os
# print(os.getcwd()) # current working firectory 현재 작업 공간
# os.chdir("rpa_basic") # rpa_basic 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())

# open("파일 경로") as f ....
print(os.path.join(os.getcwd(), "my_file.txt"))

