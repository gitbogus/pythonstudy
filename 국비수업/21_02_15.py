import csv
f = open("pharm_2019.csv", 'r', encoding='utf-8')
# csv.reader() 함수는 iterator 타입인 reader 객체를 리턴
rdr = csv.reader(f)
next(rdr) # 헤더 건너뛰기
for line in rdr:
    # if line[1] == '경주시' and line[0] == '신대원약국':
    # if line[2] == '경기도' and line[0] == '약국':
    if '수지' in line[2] and '용인' in line[2] and '로얄스포츠' in line[2]: # 포함여부 비교
    # if '경기도' in line[2] and '약국' in line[0]:
        print(line[0], line[1], line[2], line[3], sep='/')