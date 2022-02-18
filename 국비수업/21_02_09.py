import csv
 
f = open('month_temp.csv', 'r', encoding='utf-8')
# csv.reader()함수는 Iterator 타입인 reader 객체를 리턴
rdr = csv.reader(f)
header = next(rdr)
print(header)

# 각 라인은 컬럼들을 나열한 리스트(list)
for line in rdr:
    print(line)
f.close()    