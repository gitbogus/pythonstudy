import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()
ax = plt.axes()

# 직선
fig = plt.figure()
plt.plot([0, 0.2, 0.4, 0.6, 0.8, 1] * 5)

# 곡선
x = np.arange(0, 10, 0.01)
fig = plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));

# 랜덤 곡선
plt.plot(np.random.randn(50).cumsum());

# 라인스타일
plt.plot(np.random.randn(50).cumsum(), linestyle='solid')
plt.plot(np.random.randn(50).cumsum(), linestyle='dashed')
plt.plot(np.random.randn(50).cumsum(), linestyle='dashdot')
plt.plot(np.random.randn(50).cumsum(), linestyle='dotted')

# 색상 스타일

plt.plot(np.random.randn(50).cumsum(), color='red')
plt.plot(np.random.randn(50).cumsum(), color='dodgerblue')
plt.plot(np.random.randn(50).cumsum(), color='blue')
plt.plot(np.random.randn(50).cumsum(), color='black')

# 라인스타일 + 색상

plt.plot(np.random.randn(50).cumsum(), 'b-')
plt.plot(np.random.randn(50).cumsum(), 'g--')
plt.plot(np.random.randn(50).cumsum(), 'c-.')
plt.plot(np.random.randn(50).cumsum(), 'm:')

# 플롯 축

plt.plot(np.random.randn(50))
plt.xlim(-1, 50)
plt.ylim(-5, 5);

# 플롯 축 다른방법

plt.plot(np.random.randn(50))
plt.axis([-1, 50, -5, 5]);
plt.axis('tight')
plt.axis('equal')

# 플롯 레이블

plt.plot(np.random.randn(50))
plt.title("title")
plt.xlabel("x")
plt.ylabel("random.randn")

plt.plot(np.random.randn(50), label='A')
plt.plot(np.random.randn(50), label='B')
plt.plot(np.random.randn(50), label='C')
plt.title("title")
plt.xlabel("x")
plt.ylabel("y")
plt.ylabel("random.randn")
plt.legend();

# 폰트 관리자

set([f.name for f in mpl.font_manager.fontManager.ttflist])

font1 = {'family' : 'Dejavu Sans', 'size':24, 'color': 'black'}
font2 = {'family' : 'Yet R', 'size':24, 'weight':'bold', 'color': 'black'}
font3 = {'family' : 'Tahoma', 'size':16, 'weight':'light', 'color': 'black'}

plt.plot([1,2,3,4,5], [1,2,3,4,5])
plt.title('title', fontdict=font1)
plt.xlabel("xlabel", fontdict=font2)
plt.ylabel("ylabel", fontdict=font3)


# 플롯 범례(plot legend)

