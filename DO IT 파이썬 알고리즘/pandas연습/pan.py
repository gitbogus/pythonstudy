import numpy as np
import pandas as pd
# pd.__version__

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
print(s)

s. values

s.index

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
                index = ['a', 'b', 'c', 'd', 'e'])
print(s)

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
                index = [2, 4, 6, 8, 10])

print(s)

s.value_counts()

s.isin([0.25, 0.75])

pop_tuple = {'서울특별시' : 9720846,
             '부산광역시' : 3404423,
             '인천광역시' : 2947217,
             '대구광역시' : 2427954,
             '대전광역시' : 1471040,
             '광주광역시' : 1455048}

population = pd.Series(pop_tuple)
population

# dataframe 객체(2차원 특성)
pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A':4, 'B':5, 'C':7}])

pd.DataFrame(np.random.rand(5, 5),
            columns = ['A', 'B', 'C', 'D', 'E'],
            index = [1, 2, 3, 4, 5])


male_tuple = {'서울특별시' : 4732275,
             '부산광역시' : 1668618,
             '인천광역시' : 1476813,
             '대구광역시' : 1198815,
             '대전광역시' : 734441,
             '광주광역시' : 720060}

male = pd.Series(male_tuple)
male

female_tuple = {'서울특별시' : 4988571,
             '부산광역시' : 1735805,
             '인천광역시' : 1470404,
             '대구광역시' : 1229139,
             '대전광역시' : 736599,
             '광주광역시' : 734988}

female = pd.Series(female_tuple)
female

korea_df = pd.DataFrame({'인구수' : population,
                        '남자인구수' : male,
                        '여자인구수' : female})
korea_df


korea_df.index
korea_df.columns
korea_df['여자인구수']

korea_df['서울특별시':'인천광역시']

idx = pd.Index([2, 4, 6, 8, 10])
idx

idx[1]
idx[1:2:2]

print(idx)
print(idx.size)
print(idx.shape)
print(idx.ndim)
print(idx.dtype)

# index 연산

idx1 = pd.Index([1, 2, 4, 6, 8])
idx2 = pd.Index([2, 4, 5, 6, 7])
print(idx1.append(idx2))
print(idx1.difference(idx2))
print(idx1 - idx2)
print(idx1.intersection(idx2))
print(idx1 & idx2)
print(idx1.union(idx2))
print(idx1 | idx2)
print(idx1.delete(0))
print(idx1.drop(1))
print(idx1 ^ idx2)

# 인덱싱

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
                index = ['a','b','c','d','e'])
s

s['b']

s.keys()

list(s.items())

s['f'] = 1.25
s

s['a':'d']
s[0:4]

s[(s > 0.4) & (s < 0.8)]

# Series 인덱싱

s = pd.Series(['a','b','c','d','e'],
                index=[1, 3, 5, 7, 9])
s

s[1]
s[2:4]
s.iloc[1]
s.iloc[2:4]
s.reindex(range(10))

s.reindex(range(10), method='bfill')

# DataFrame 인덱싱

korea_df['남여비율'] = (korea_df['남자인구수'] * 100 / korea_df['여자인구수'])
korea_df.남여비율
korea_df.values
korea_df.T
korea_df['인구수']
korea_df.loc[:'인천광역시', : '남자인구수'] # 문자로 접근
korea_df.loc[(korea_df.여자인구수 > 1000000)]
korea_df.loc[(korea_df.인구수 < 2000000)]
korea_df.loc[(korea_df.인구수 < 2500000)]
korea_df.loc[korea_df.남여비율 > 100]
korea_df.loc[(korea_df.인구수 > 2500000) & (korea_df.남여비율 > 100)]
korea_df.iloc[:3, :2] # 정수로 접근

idx_tuples = [('서울특별시', 2010), ('서울특별시' , 2020),
              ('부산광역시', 2010), ('부산광역시' , 2020),
              ('인천광역시', 2010), ('인천광역시' , 2020),
              ('대구광역시', 2010), ('대구광역시' , 2020),
              ('대전광역시', 2010), ('대전광역시' , 2020),
              ('광주광역시', 2010), ('광주광역시' , 2020)]
idx_tuples

pop_tuples = [10312545, 9720846,
              2567910,  3404423,
              2578296,  2947217,
              2511676,  2427954,
              1503664,  1471040,
              1454636,  1455048]
population = pd.Series(pop_tuples, index = idx_tuples)
population

mdix = pd.MultiIndex.from_tuples(idx_tuples)
print(mdix)

populatiun = population.reindex(mdix)
population

# population[:, 2010]

# population['대전광역시', :]

korea_mdf = population.unstack()
korea_mdf

korea_mdf.stack()

male_tuples = [5111259, 4732275,
              1773170, 1668618,
              1390356, 1476813,
              1255245, 1198815,
              753648,  734441,
              721780,  720060]
male_tuples

korea_mdf = pd.DataFrame({'총인구수' : population,
                          '남자인구수' : male_tuples})
korea_mdf

female_tuples = [5201286, 4988571,
                 1794740, 1735805,
                 1367940, 1470404,
                 1256431, 1229139,
                 750016,  736599,
                 732856,  734988]
female_tuples

korea_mdf = pd.DataFrame({'총인구수' : population,
                          '남자인구수' : male_tuples,
                          '여자인구수' : female_tuples})
korea_mdf

ratio = korea_mdf['남자인구수'] * 100 / korea_mdf['여자인구수']
ratio

ratio.unstack()

korea_mdf = pd.DataFrame({'총인구수' : population,
                          '남자인구수' : male_tuples,
                          '여자인구수' : female_tuples,
                          '남여비율' : ratio})
korea_mdf

# 다중 인덱스 생성

df = pd.DataFrame(np.random.rand(6, 3),
                  index = [['a','a','b','b','c','c'],[1, 2, 1, 2, 1, 2]],
                  columns = ['c1', 'c2', 'c3'])
df

pd.MultiIndex.from_arrays([['a','a','b','b','c','c'],[1, 2, 1, 2, 1, 2]])

pd.MultiIndex.from_poduct([['a','b','c'],[1, 2]])

pd.MultiIndex(levels=[['a', 'b', 'c'], [1, 2]],
              codes = [[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])

population

population.index.names = ['행정구역', '년도']
population

idx = pd.MultiIndex.from_product([['a','b','c'], [1, 2]],
                                 names = ['name1', 'name2'])
cols = pd.MultiIndex.from_product([['c1', 'c2', 'c3'], [1, 2]],
                                   names = ['col_name1', 'col_name2'])
data = np.round(np.random.randn(6, 6), 2)
mdf = pd.DataFrame(data, index = idx, columns=cols)
mdf           

mdf['c2']

# 인덱싱 및 슬라이싱

population['인천광역시', 2010]

population[:, 2010]

population[population > 3000000]

population[['대구광역시', '대전광역시']]

mdf

mdf['c2', 1]

mdf.iloc[:3, :4]

mdf.loc[:, ('c2', 1)]

idx_slice = pd.IndexSlice
mdf.loc[idx_slice[:, 2], idx_slice[:, 2]]

# korea_mdf['서울특별시' : '인천광역시']

korea_mdf = korea_mdf.sort_index()
korea_mdf

korea_mdf['서울특별시' : '인천광역시']

korea_mdf.unstack(level=0)

korea_mdf.unstack(level=1)

korea_mdf.stack()

idx_flat = korea_mdf.reset_index(level =0)
idx_flat

idx_flat = korea_mdf.reset_index(level=(0, 1))
idx_flat

idx_flat.set_index(['행정구역','연도'])
