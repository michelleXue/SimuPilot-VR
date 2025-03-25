from user_action_decider.object_detection import *
from user_action_decider.actions import *
from user_action_decider.utils import *
from user_action_decider.json_action import *
from user_action_decider.end_condition import *
import time
import json

# SimuPilot VR

# Setup
# Set screenshot bounds in bounds.py
# put api key in apy_key.txt
# Enter goal in goal variable

goal = ""

time.sleep(2)

ending = False

counter = 0

while not ending:

    # take screenshot
    screenshot(counter)

    # compress screenshot
    compress_images_in_folder("temp/screenshot_original", "temp/screenshot_compressed")

    # detect objects and save to json
    target = detect_objects(f"temp/screenshot_compressed/screenshot{counter}.png", goal)

    # parse json
    jsonPath = f"screenshotjson/screenshot{counter}.json"

    with open(jsonPath, "r", encoding="utf-8") as file:
        data = json.load(file)
        json_string = json.dumps(data)

    # determine action
    print(target)
    determine_action(json_string, target)

    # Check if finished
    screenshot(counter, True)
    compress_images_in_folder("temp/screenshot_original", "temp/screenshot_compressed")
    ending = finished(goal, f"temp/screenshot_compressed/screenshotend{counter}.png")
    print(ending)
    count += 1

print("Done")
hold_key("right", 10)
