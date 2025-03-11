import time
import pyautogui


def press_w_key(times, thelddown, tinbetween):
    for _ in range(times):
        pyautogui.keyDown("w")
        time.sleep(thelddown)
        pyautogui.keyUp("w")
        time.sleep(tinbetween)


def press_key(key, times, thelddown, tinbetween):
    for _ in range(times):
        pyautogui.keyDown(key)
        time.sleep(thelddown)
        pyautogui.keyUp(key)
        time.sleep(tinbetween)


def hold_key(key, thelddown):
    pyautogui.keyDown(key)
    time.sleep(3)
    pyautogui.keyUp(key)


# hold_key(Key.W, 2)
# hold_key(Key.A, 2)
# hold_key(Key.S, 2)
# hold_key(Key.D, 2)
# hold_key(Key.RightArrow, 1)

time.sleep(3)
pyautogui.keyDown("d")
time.sleep(3)
pyautogui.keyUp("d")
