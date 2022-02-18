def job():
    print('3초마다 데이터 수집 배치작업')
    
import schedule, time

# 3초마다 데이터 수집 배치작업 계획(주기 또는 일시) 수립 정의 (일정)
# 예약
schedule.every(3).seconds.do(job)
# schedule.every(1).minute.do(job) 주기 디폴트 1
# schedule.every().hour.do(job)
# 매일마다 12시 30분에 한번씩 실행
# schedule.every().day.at('12:30').do(job)

while True: # 현재 프로그램의 중단 방지 목적
    # 예약 계획을 확인하고 예약된 모든 함수를 실행
    schedule.run_pending() 
    time.sleep(1)