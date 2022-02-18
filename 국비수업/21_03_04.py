import pandas as pd
# import numpy as np

ratings = pd.read_csv('data/rating.csv')
movies = pd.read_csv('data/movies.csv')
users = pd.read_csv('data/users.csv')

ratings.tail()
movies.tail()
users.tail()

# 공통 컬럼을 이용한 세 데이터프레임 내부조인(병합)
data = pd.merge(pd.merge(ratings, users), movies)

# ratings = pd.read_csv('data/ratings.csv') 
# movies = pd.read_csv('data/movies.csv')
# users = pd.read_csv('data/users.csv')

# ratings.tail()
# movies.tail()
# users.tail()
# # 공통 컬럼을 이용한 세 데이터프레임 내부조인(병합)
# data = pd.merge(pd.merge(ratings, users), movies)
