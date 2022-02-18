# 10진수를 다른 진법의 숫자로 변환하는 함수를 만들어보자 (2 ≤ base ≤ 10):

def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number%base * multiplier
        multiplier *= 10
        number = number//base
    return result

def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print("테스트통과")

if __name__ == "__main__":
    test_convert_from_decimal()