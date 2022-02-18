# 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 이자를 구하는 함수 simple_interest()를 작성하세요.

def simple_interest(p,r,t):
    i = p*r*t
    return ("당신의 이자는 ", i,"입니다.")
print(simple_interest(10000000, 0.03875, 5))

print(simple_interest(1100000, 0.05, 5/12))

def simple_interest_amount(p, r, t):
    return p * (1 + r * t)

print(simple_interest_amount(10000000, 0.03875, 5))