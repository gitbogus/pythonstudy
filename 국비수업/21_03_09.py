import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='MaLgun Gothic')

tips = sns.load_dataset("tips")  # 팁 데이터셋(DataFrame)

sns.barplot(x='day', y='total_bill', data=tips)
plt.title("요일 별 전체팀(팀포함 식사대금)")
plt.savefig('day.png')
#hue = 카테고리 = 별
sns.barplot(x='day', y='total_bill', hue='sex', data=tips)
plt.title('요일별, 성별 전체팀')

# 오차막대에 신뢰구간이 아니라 표준편차를 표현 ci='sd'
# 오차막대 미출력 ci=None
sns.barplot(x='day', y='total_bill',hue='sex', data=tips,ci='sd')
plt.title("요일별, 성별 전체 팀")
# estimator=np.median 평균 아니라 중위수로 계산
sns.barplot(x='day', y='total_bill', hue='sex', data=tips,
            estimator=np.median,ci="sd")