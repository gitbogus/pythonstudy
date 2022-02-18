import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

# result = 0
# for number in numbers:
#     result += int(number)
# print(result)
#",".join(['1','2'])

from functools import reduce
b = list(map(int, " ".join(numbers).split())) #int('1')
print(reduce(lambda x,y:x+y, b)/len(b))#print해서 외부콘솔창에 출력
