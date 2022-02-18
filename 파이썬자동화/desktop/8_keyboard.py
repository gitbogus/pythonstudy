import pyautogui

w = pyautogui.getWindowsWithTitle("메모장")[0] # 메모장 1개띄운상태로 갖고옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval = 0.25)

# t e s t 순서대로 적고 왼쪽 2번 오른쪽 1번 l a 적고 엔터
# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval = 0.25)

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키 ( Hot key )
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 >  Shift 떼고 > Alt 떼고 > ctrl 떼고

import pyperclip
pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여 넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
my_write("나도 코딩")