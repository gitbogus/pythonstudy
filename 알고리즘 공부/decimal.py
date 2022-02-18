a = sum(0.1 for i in range(10)) == 1.0
print(a)

import decimal
b = sum(decimal.Decimal("0.1") for i in range(10)) == decimal.Decimal("1.0")
print(b)