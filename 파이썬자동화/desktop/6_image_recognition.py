import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# filefile = pyautogui.locateOnScreen("filefile.png")
# pyautogui.moveTo(filefile)

# 반복 작업

# for i in pyautogui.locateAllOnScreen ("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration = 0.25)

# 한번

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)


# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()

# 1824,54 54,55,55 #363737

# 1824,1032 0,122,204 #007ACC

# 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region = (1824,54, 204-55))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence = 0.9) # 90%
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우



# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견실패")

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen(file_menu_notepad)
#     print("발견실패")
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (timeout)
file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time()
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()  # 종료 시간 설정
#     if end - start > timeout : # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit

# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Time {timeout}s] Target not found ({img_file}). Terminate program")
        sys.exit()

my_click("file_menu_notepad.png", 10)