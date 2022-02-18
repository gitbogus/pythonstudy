import csv
f = open("pharm_2019.csv", 'r', encoding='utf-8')
# csv.reader() 함수는 iterator 타입인 reader 객체를 리턴
rdr = csv.reader(f)
next(rdr) # 헤더 건너뛰기
recent = 0 # 약국수
for line in rdr:
    if int(line[3]) > 20160215:
        recent+=1
print("최근 5년 이내 개설 약국 수 : %d개" %recent)