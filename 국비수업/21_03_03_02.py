iris3.csv와 iris4.csv 데이터셋을 pandas로 
탐색적 데이터 분석을 한다.

import pandas as pd

1. 두 파일을 각각 pandas DataFrame으로 읽어서 
하나의 DataFrame으로 합치는 코드를 작성한다.  
#%%
df_iris3 = pd.read_csv("iris3.csv", encoding="utf-8")
df_iris4 = pd.read_csv("iris4.csv", encoding="utf-8")

df = pd.concat([df_iris3,df_iris4], ignore_index=True)
#%%

2. 데이터 프레임의 처음, 마지막 3개 데이터를 출력후
데이터 프레임의 구조 및 컬럼별 요약 통계량을 출력한다. 
#%%
df.head(3)
df.tail(3)
df.shape
df.info()
df.describe()
#%%

3. 마지막 속성 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica' 
꽃 품종 분류이름을 각각 0,1,2로 재레이블링(정수인코딩)한다.  
#%%
df['species'] \
=df['species'].astype('category')
df['species'].cat.categories=[0,1,2]

'''
x = df.iloc[:,-1] == 'Iris-setosa'
y = df.iloc[:,-1] == 'Iris-versicolor'
z = df.iloc[:,-1] == 'Iris-virginica' 

df.loc[x,"species"] = 0
df.loc[y,"species"] = 1
df.loc[z,"species"] = 2
'''



df
4. sepal_length와 sepal_width  컬럼의 평균을 출력한 후 
꽃 품종이름별로 그룹을 만들어서 sepal_length 컬럼의 평균을 출력한다
#%%
df["sepal_length"].mean()
df["sepal_width"].mean()
df.groupby("species")["sepal_length"].mean()
species와 sepal_length 상관성 발견

#%%

5.꽃 품종이름을 기준으로 삼아 오름차순이 되도록 행들을 정렬한다.
#%%
df.sort_values(by="species")
#%%
6. petal_length가 2.45 이하인 행들의 꽃 품종이 
모두 'Iris-Setosa'(0) 인지 간단히 정량분석해보는 코드를 작성한다. 
#%%
df2=df[df.iloc[:,2] <= 2.45]
df2.iloc[:,-1].unique()
df2.iloc[:,-1].value_counts()
'''
0    50
2     0
1     0
'''
#%%

7. 행마다  4열 크기 속성값들을  최대값으로 요약하여 1차원으로
차원을 축소하고자 한다.
최대값을 출력하여 이 값으로 해당 벡터의 주성분으로 정의한다.

#%%
main_value = df.iloc[:,:4].max(axis=1)
main_value
