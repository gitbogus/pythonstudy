import pyautogui
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 57,16 22,133,208 #1685D0

pixel = pyautogui.pixel(57, 16)
print(pixel)

print(pyautogui.pixelMatchesColor(57, 16, (22,133,208)))
