# A.format()은 문자열 A에 변수를 추가하거나 형식화 하는데 사용한다.

import decimal 
print("{0} {0!s} {0!r} {0!a}").format(decimal.Decimal("99.9"))