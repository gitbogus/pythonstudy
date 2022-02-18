def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

def wow_f(x, y):
    return (x + y) * const

wow_f(3, 2)

def wow_f(x, y, const = 0.1):
    return(x + y) * const

wow_f(3,5)

