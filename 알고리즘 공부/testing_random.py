# import random

# def testing_random():
#     """랜덤 모듈 테스트"""
#     values = [1, 2, 3, 4]
#     print(random.choice(values))
#     print(random.choice(values))
#     print(random.choice(values))
#     print(random.sample(values, 2))
#     print(random.sample(values, 3))

#     """ values 리스트를 섞는다 """
#     random.shuffle(values)
#     print(values)

#     """ 0~10의 임의의 정수를 생성한다"""
#     print(random.randint(0, 10))
#     print(random.randint(0, 10))

# if __name__ == "__main__":
#     testing_random()

# import random

# def lotto_random():
#     """로또 랜덤번호생성기"""
#     values = range(1,46)
#     print("행운의 번호는")
#     print(random.sample(values, 6))
#     print(random.sample(values, 6))
#     print(random.sample(values, 6))
#     print(random.sample(values, 6))
#     print(random.sample(values, 6))

# if __name__ == "__main__":
#     lotto_random()


from random import *

num = range(1, 46)

num = list(num)

 

for i in range(1, 6) : 

    shuffle(num)

    lottoN = sample(num, 6)

    lottoN.sort()

    print(f'{i}번째 {lottoN}')

