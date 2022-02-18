import csv

f = open('hospital_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)
print("번호", '치과병원명', header[3], header[6])

number = 1
for line in lines:
    if line[1] == "치과병원" and line[2] == "전남":
        print('%d. ' % number, end='')
        print(line[0], line[3], line[6], sep='/')
        number += 1

f.close()