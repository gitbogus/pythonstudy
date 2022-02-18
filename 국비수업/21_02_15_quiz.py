# 1. 제주도에서 2016~2018년 3년간 개원(개설)한 의사수를 구해본다.
# *출력결과
# 2016~2018년 3개년간 개원한 제주도의 의원 수 : 104개

# import csv

# f = open('hospital_2019.csv', 'r', encoding='utf-8')
# lines = csv.reader(f)

# header = next(lines)
# print("번호", '병원명', header[3], header[6])

# number = 0
# for line in lines:
#     if "제주" in line[2] and line[5] >= "20160101" and line[5] <= "20181231":
#         print('%d. ' % number, end='')
#         print(line[0], line[3], line[6], sep='/')
#         number += 1

# print("2016~2018년 3개년간 제주도의 의원수 : {0}개".format(number))
# f.close()

# 2. 부산의 병원명에 '삼성'이 들어가는 병원에 대해 총 병원수와 
# 병원명,종류,주소의 목록을 출력해본다.
# *출력결과일부
# 번호  병원명 종류 주소 개설일자
# 1. 덕천삼성정형외과의원/의원/부산광역시 북구 만덕대로 58 3층 (덕천동)/20170427
# 2. 르노삼성자동차부속의원/의원/부산광역시 강서구 르노삼성대로 61 (신호동)/20140827
# 3. 비에스(BS)삼성안과의원/의원/부산광역시 중구 구덕로 90 (남포동6가)/20131101


import csv

f = open('hospital_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)
print("번호", '병원명', header[3], header[6])

number = 0
for line in lines:
    if "부산" in line[2] and "삼성" in line[0]:
        print('%d. ' % number, end='')
        print(line[0], line[3], line[6], sep='/')
        number += 1

print("부산의 병원명에 삼성이 들어가는 병원 : {0}개".format(number))
f.close()

# 2. 부산의 병원명에 '삼성'이 들어가는 병원에 대해 총 병원수와 
# 병원명,종류,주소,개설일자의 목록을 출력해본다.
# *출력결과일부
# 번호  병원명 종류 주소 개설일자
# 1. 덕천삼성정형외과의원/의원/부산광역시 북구 만덕대로 58 3층 (덕천동)/20170427
# 2. 르노삼성자동차부속의원/의원/부산광역시 강서구 르노삼성대로 61 (신호동)/20140827
# 3. 비에스(BS)삼성안과의원/의원/부산광역시 중구 구덕로 90 (남포동6가)/20131101

