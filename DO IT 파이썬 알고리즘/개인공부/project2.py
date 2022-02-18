import sys
import shutil

shutil.copy('.\\contact_db.txt', '.\\contact_db_backup.txt')
print("백업이 완료되었습니다. 프로그램을 종료합니다.")
sys.exit()