# Q1 문자열 바꾸기
# 다음과 같은 문자열이 있다.

# a:b:c:d
# 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.
#a#b#c#d

# lst = "a:b:c:d"
# b = lst.split(":")
# print(b)
# c = "#".join(b)
# print(c)

# Q2 딕셔너리 값 추출하기
# 다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.

# >>> a = {'A':90, 'B':80}
# >>> a['C']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'C'
# a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다. 'C'에 해당하는 key 값이 없을 경우 오류 대신 70을 얻을 수 있도록 수정하시오.

# a = {'A': 90 , 'B':80}
# # print(a['C'])
# a.update({'C':70})
# print(a['C'])

# 딕셔너리의 get 함수를 사용하면 해당 key가 없을 경우에는 두 번째 매개변수로 전달된 default 값을 대신 돌려준다.

# >>> a = {'A':90, 'B':80}
# >>> a.get('C', 70)
# 70
# 위 예에서는 'C'에 해당되는 key가 없기 때문에 디폴트 값으로 전달된 70을 돌려주었다.

# Q3 리스트의 더하기와 extend 함수
# 다음과 같은 리스트 a가 있다.

# >>> a = [1, 2, 3]
# 리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.

# >>> a = [1, 2, 3]
# >>> a = a + [4,5]
# >>> a
# [1, 2, 3, 4, 5]
# 리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.

# >>> a = [1, 2, 3]
# >>> a.extend([4, 5])
# >>> a
# [1, 2, 3, 4, 5]
# + 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.

# a = [1, 2, 3]
# a = a + [4, 5] # 주소값이 변함
# print(id(a))
# a.extend([4, 5]) # 주소값이 변하지 않음
# print(id(a))

# Q4 리스트 총합 구하기
# 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.

# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# result = 0
# while A:
#     mark = A.pop()
#     if mark >= 50:
#         result += mark
# print(result)

# 리스트 총합 구하기

# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# result = 0
# while A:                # A 리스트에 값이 있는 동안
#     mark = A.pop()      # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
#     if mark >= 50:      # 50점 이상의 점수만 더함
#         result += mark

# print(result)           # 481 출력

# Q5 피보나치 함수
# 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.

# 0, 1, 1, 2, 3, 5, 8, 13, ...
# 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.

# def fibonacci_iterator(n):
#     if n < 2: return
#     a, b = 0, 1
    
#     for i in range(n):
#         a, b = b, a + b
#         print("{0} ".format(a), end = "")
        
#     print()

# def fibonacci_generator(n):
#     a, b = 0, 1
#     while True:
#         yield b
#         a, b = b, a + b
 
# def display_fibonacci():
#     str = input("수열 갯수를 입력하세요 :")
#     n = int(str)
    
#     # for 문을 이용한 피보나치 수열
#     print("for statement fibonacci :")
#     fibonacci_iterator(n)
    
#     # Generator 를 이용한 피보나치 수열
#     print("Using generator fibonacci :")
#     fib_gen = fibonacci_generator(n)
#     for _ in range(n):
#         print(next(fib_gen), end=" ")

# if __name__ == "__main__":
#     display_fibonacci()

# Q6 숫자의 총합 구하기
# 사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)

# 65,45,2,3,45,8
# number = input("숫자를 입력하세요 : ")
# numbers = number.split(",")
# result = 0
# for i in numbers:
#     result += int(i) #+ result
# print(result)

# 숫자의 총합 구하기

# user_input = input("숫자를 입력하세요: ")
# numbers = user_input.split(",")
# total = 0
# for n in numbers:
#     total += int(n)    # 입력은 문자열이므로 숫자로 변환해야 한다.
# print(total)

# Q7 한 줄 구구단
# 사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오.

# 실행 예)

# 구구단을 출력할 숫자를 입력하세요(2~9): 2
# 2 4 6 8 10 12 14 16 18

# gugu = int(input("출력할 숫자를 입력하세요 : "))

# for i in range(1,10):
#     print( i * gugu, end=' ' )

# Q8 역순 저장
# 다음과 같은 내용의 파일 abc.txt가 있다.

# AAA
# BBB
# CCC
# DDD
# EEE
# 이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

# EEE
# DDD
# CCC
# BBB
# AAA

# 역순 저장

# 파일 객체의 readlines를 사용하여 모든 라인을 읽은 후에 reversed를 사용하여 역순으로 정렬한 다음 다시 파일에 저장한다.

# f = open('abc.txt', 'r')
# lines = f.readlines()    # 모든 라인을 읽음
# f.close()

# lines.reverse()          # 읽은 라인을 역순으로 정렬

# f = open('abc.txt', 'w')
# for line in lines:
#     line = line.strip()  # 포함되어 있는 줄 바꿈 문자 제거
#     f.write(line)
#     f.write('\n')        # 줄 바꿈 문자 삽입
# f.close()

# Q9 평균값 구하기
# 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 
# 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.

# 70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100

# Q9.

# 평균 값 구하기

# f = open("sample.txt")
# lines = f.readlines( )  # sample.txt를 줄 단위로 모두 읽는다.
# f.close( )

# total = 0
# for line in lines:
#     score = int(line)  # 줄에 적힌 점수를 숫자형으로 변환한다.
#     total += score
# average = total / len(lines)

# f = open("result.txt", "w")
# f.write(str(average))
# f.close()

# sample.txt의 점수를 모두 읽기 위해 파일을 열고 readlines를 사용하여 각 줄의 점수 값을 모두 읽어 들여 총 점수를 구한다. 
# 총 점수를 sample.txt 파일의 라인(Line) 수로 나누어 평균 값을 구한 후 그 결과를 result.txt 파일에 쓴다. 
# 숫자 값은 result.txt 파일에 바로 쓸 수 없으므로 str 함수를 사용하여 문자열로 변경한 후 파일에 쓴다.

# Q10 사칙연산 계산기
# 다음과 같이 동작하는 클래스 Calculator를 작성하시오.

# >>> cal1 = Calculator([1,2,3,4,5])
# >>> cal1.sum() # 합계
# 15
# >>> cal1.avg() # 평균
# 3.0
# >>> cal2 = Calculator([6,7,8,9,10])
# >>> cal2.sum() # 합계
# 40
# >>> cal2.avg() # 평균
# 8.0

# class Calculator:
#     def __init__(self, numberlist):
#         self.numberlist = numberlist
        

# def sum(self):
#     result = 0
#     for num in self.numberlist:
#         result += num
#         return result
    
# def avg(self):
#     total = self.sum()
#     return total / len(self.numberlist)

# cal1 = Calculator([1,2,3,4,5]) 
# print (cal1.sum())
# print (cal1.avg())

# # Q10.

# # 사칙연산 계산기

# class Calculator:
#     def __init__(self, numberList): 
#         self.numberList = numberList

#     def sum(self): 
#         result = 0
#         for num in self.numberList: 
#             result += num
#         return result

#     def avg(self):
#         total = self.sum()
#         return total / len(self.numberList)

# cal1 = Calculator([1,2,3,4,5]) 
# print (cal1.sum())
# print (cal1.avg())

# # cal2 = Calculator([6,7,8,9,10]) 
# # print (cal2.sum())
# # print (cal2.avg())

# Q12 오류와 예외 처리
# 다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.

# result = 0

# try:
#     [1, 2, 3][3]
#     "a"+1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4

# print(result)

# Q13 DashInsert 함수
# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오.

# 입력 예시: 4546793
# 출력 예시: 454*67-9-3
# data = "4546793"
# numbers = list(map(int, data))   # 숫자 문자열을 숫자 리스트로 변경
# result = []

# for i, num in enumerate(numbers):
#     result.append(str(num))
#     if i < len(numbers)-1:                   # 다음 수가 있다면
#         is_odd = num % 2 == 1                # 현재 수가 홀수
#         is_next_odd = numbers[i+1] % 2 == 1  # 다음 수가 홀수
#         if is_odd and is_next_odd:           # 연속 홀수
#             result.append("-")
#         elif not is_odd and not is_next_odd: # 연속 짝수
#             result.append("*")

# print("".join(result))


# Q14 문자열 압축하기
# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.

# 입력 예시: aaabbcccccca
# 출력 예시: a3b2c6a1

# def compress_string(s):
#     _c = ""
#     cnt = 0
#     result = ""
#     for c in s:
#         if c!=_c:
#             _c = c
#             if cnt: result += str(cnt)
#             result += c
#             cnt = 1
#         else:
#             cnt +=1
#     if cnt: result += str(cnt)
#     return result

# print (compress_string("aaabbcccccca"))  # a3b2c6a1 출력

