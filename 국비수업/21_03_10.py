names_file = glob.glob('data/names/yob201*')
names=pd.DataFrame() # 통합DF
for fname in names_file:
    df= pd.read_table(fname,header=None
                      ,names=['name','gender','count'],sep=',')
    df['year'] =fname[14:18] #연도4자리
    #파일경로 리스트 df 합치기 
    names=pd.concat([names,df],ignore_index=True)
    
names.head()


