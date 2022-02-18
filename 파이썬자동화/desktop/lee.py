import pyautogui
import pyperclip
pyautogui.PAUSE = 0.2


# pyautogui.mouseInfo()
# pyautogui.moveTo(670, 362, duration=0.25)
# pyautogui.click(670, 362)
# pyautogui.typewrite('1', interval=0.1)
# pyautogui.moveTo(964, 360, duration=0.25)
# pyautogui.click(964, 360)
# pyautogui.typewrite('2', interval=0.1)
# pyautogui.moveTo(1262, 382, duration=0.25)
# pyautogui.click(1262, 382)
# pyautogui.moveTo(662, 625, duration=0.25)
# pyautogui.click(662, 625)
# pyautogui.moveTo(962, 621, duration=0.25)
# pyautogui.click(962, 621)
# pyautogui.moveTo(1260, 621, duration=0.25)
# pyautogui.click(1260, 621)
# pyautogui.moveTo(672, 877, duration=0.25)
# pyautogui.click(672, 877)
# pyautogui.moveTo(968, 879, duration=0.25)
# pyautogui.click(968, 879)
# pyautogui.moveTo(1266, 883, duration=0.25)
# pyautogui.click(1266, 883)

# pyautogui.click(300, 300)
# pyautogui.scroll(-400)
pyautogui.moveTo(670, 362, duration=0.25)
e = 137
for i in range(2):
    pyautogui.move(300, 0)
    pyautogui.click()
    pyautogui.typewrite(f'{e}', interval=0.3)
    e += 1
    if e == 139: # +15   
        pyautogui.moveTo(662, 625, duration=0.25)
        pyautogui.click()
        pyautogui.typewrite(f'{e}', interval=0.3)
        e += 1
        for i in range(2):
            pyautogui.move(300, 0)
            pyautogui.click()
            pyautogui.typewrite(f'{e}', interval=0.3)
            e += 1
            if e == 142: # +15
                pyautogui.moveTo(672, 877, duration=0.25)
                pyautogui.click()
                pyautogui.typewrite(f'{e}', interval=0.3)
                e += 1
                for i in range(2):
                    pyautogui.move(300, 0)
                    pyautogui.click()
                    pyautogui.typewrite(f'{e}', interval=0.3)
                    e += 1
                    if e == 145: # +15
                        pyautogui.scroll(-800)
                        pyautogui.moveTo(670, 383, duration=0.25)
                        pyautogui.click()
                        pyautogui.typewrite(f'{e}', interval=0.3)
                        e += 1
                        for i in range(2):
                            pyautogui.move(300, 0)
                            pyautogui.click()
                            pyautogui.typewrite(f'{e}', interval=0.3)
                            e += 1
                            if e == 148: #+15
                                pyautogui.moveTo(670,642, duration=0.25)
                                pyautogui.click()
                                pyautogui.typewrite(f'{e}', interval=0.3)
                                e += 1
                                for i in range(2):
                                    pyautogui.move(300, 0)
                                    pyautogui.click()
                                    pyautogui.typewrite(f'{e}', interval=0.3)
                                    e += 1