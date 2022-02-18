import numpy as np
import pandas as pd

s = pd.Series(np.random.randint(0, 10, 5))
s

df = pd.DataFrame(np.random.randint(0, 10, (3, 3)),
                  columns = ['A', 'B', 'C'])
df

np.exp(s)

# cos값
np.cos(df * np.pi / 4)

s1 = pd.Series([1, 3, 5, 7, 9], index = [0, 1, 2, 3, 4])
s2 = pd.Series([2, 4, 6, 8, 10], index = [1, 2, 3, 4, 5])
s1 + s2

s1.add(s2, fill_value = 0)
df1 = pd.DataFrame(np.random.randint(0, 20, (3, 3)),
                    columns = list('ACD'))
df1

df2 = pd.DataFrame(np.random.randint(0, 20, (5, 5)),
                   columns=list('BAECD'))
df2

df1 + df2

fvalue = df1.stack().mean()
df1.add(df2, fill_value=fvalue)

# 연산자 범용 함수

a = np.random.randint(1, 10, size = (3, 3))
a

a + a[0]

df = pd.DataFrame(a, columns=list('ABC'))
df

df + df.iloc[0]

df.add(df.iloc[0])
