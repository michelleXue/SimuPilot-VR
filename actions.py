import time
import pyautogui as pag


# Press key
def press_key(key, times, thelddown, tinbetween):
    for _ in range(times):
        pag.keyDown(key)
        time.sleep(thelddown)
        pag.keyUp(key)
        time.sleep(tinbetween)


# hold key
def hold_key(key, dur):
    pag.keyDown(key)
    time.sleep(dur)
    pag.keyUp(key)


# Action to button mappings


def move_forward(duration):
    hold_key("w", duration)


def move_left(duration):
    hold_key("a", duration)


def move_right(duration):
    hold_key("d", duration)


def in_place_rotate_to_left(duration):
    hold_key("left", duration)


def in_place_rotate_to_right(duration):
    hold_key("right", duration)


def look_up(duration):
    hold_key("up", duration)


def look_down(duration):
    hold_key("down", duration)


def press_button(duration):
    hold_key("u", duration)


<<<<<<< Updated upstream:actions.py
def screenshot(counter):
    # Define the bounding box (left, top, width, height)
    region = (624, 31, 1356, 1488)  # Captures a 500x400 area starting from (100,100)
=======
# take screenshots
def screenshot(counter, end=False):
    # Define the bounding box from bounds.by (left, top, width, height)
    region = (1329, 109, 1224, 1337)
>>>>>>> Stashed changes:user_action_decider/actions.py

    # Take a screenshot of the specified region
    screenshot = pag.screenshot(region=region)

    # Save the screenshot
<<<<<<< Updated upstream:actions.py
    screenshot.save(f"screenshot{counter}.png")
=======
    if end:
        screenshot.save(f"temp/screenshot_original/screenshotend{counter}.png")
    else:
        screenshot.save(f"temp/screenshot_original/screenshot{counter}.png")
>>>>>>> Stashed changes:user_action_decider/actions.py
    return screenshot
