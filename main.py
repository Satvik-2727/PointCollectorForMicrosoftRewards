# import mouse # pip install mouse
# import time

# time.sleep(8)
# for i in range(200000):
#         mouse.click("left")
import keyboard
# import pyautogui
import time
import mouse
for i in range(31):
    time.sleep(4)
    if i>0 and i%10==0:
        for i in range(10):
            mouse.click("left")
            time.sleep(2)
            keyboard.press_and_release("ctrl+w")
    keyboard.write(str(i))
    keyboard.press("enter")
    time.sleep(2)
    keyboard.press_and_release("ctrl+t")