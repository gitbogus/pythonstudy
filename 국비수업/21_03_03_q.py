data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
'year': ['2014', '2015', '2016', '2015', '2016'],
"points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)

import pandas as pd

# CSV 파일을 읽어 들여 frame에 저장후 정제  
frame = pd.read_csv("population_2020.csv", encoding="utf-8")    
#1, 2, 4, 5 열의 ','와 공백문자를 제거 후 정수 형변환
frame.iloc[:, [1, 2, 4, 5]]
#컬럼이름이 한글이고 조금 복잡 -> 정수인덱스로 산출 
frame.iloc[:,1]=frame.iloc[:,1].str.replace(',', '').replace(' ', '').astype('int64')
frame.iloc[:,2]=frame.iloc[:,2].str.replace(',', '').replace(' ', '').astype('int64')
frame.iloc[:,4]=frame.iloc[:,4].str.replace(',', '').replace(' ', '').astype('int64')
frame.iloc[:,5]=frame.iloc[:,5].str.replace(',', '').replace(' ', '').astype('int64')
frame2 = frame.iloc[:, [1, 2, 4, 5]]
           
# sum() 메소드로 행 방향으로 합계를 구함
sum = frame2.sum(axis=0)
sum

loan = pd.read_csv("data/loan.csv")

df2=loan[["loan_amnt", "loan_status", "grade", "int_rate", "term"]]
df2= df2.dropna(how="any")
df2.head()
#기간(term)에 따른 대출 총액 사전
term_to_loan_amnt_dict = {}
uniq_terms = df2["term"].unique()
uniq_terms#array([' 36 months', ' 60 months'], dtype=object)
for	term	in	uniq_terms:
				loan_amnt_sum	=	df2.loc[df2["term"]	==	term,	"loan_amnt"].sum()
				term_to_loan_amnt_dict[term]	=	loan_amnt_sum

term_to_loan_amnt_dict
