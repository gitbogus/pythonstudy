import numpy as np
movie_data = np.loadtxt('data/rating.csv', delimiter=',',skiprows=1)
movie_data[:5,:]
movie_data.shape

# 평균 평점
np.mean(movie_data[:,2])
movie_data[:2].mean()
#userId
userids = np.unique(movie_data[:,0]) #중복 요소 제거
userids.shape #(610,)

# 사용자별 평균 평점 리스트
# [userId,평균 평점]를 추가 저장
mean_rating_by_user_list = []




reverse_rating = np.sort(mean_rating_by_user_array[:,1])[::-1]
th=reverse_rating[int(0.2 * len(mean_rating_by_user_array[:,1]))]
mean_rating_by_user_array_20 =  reverse_rating[reverse_rating>=th]
[(int(x),y) for x,y in mean_rating_by_user_array if y in mean_rating_by_user_array_20]
