#플롯 한글 깨짐방지 
plt.rc('font', family='Malgun Gothic') 
labels = ['개구리', '돼지', '개', '고양이'] #요소
sizes = [15, 30, 45, 10] # 요소값의 비율, 요소합이 100을 넘으면 자동 비율 계산
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0) #다른요소와의 간격
plt.title("Pie Chart")
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90) #90도부터 개구리,돼지 이런순서
