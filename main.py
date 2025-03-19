from user_action_decider.object_detection import *
from user_action_decider.actions import *
from user_action_decider.utils import *
from user_action_decider.json_action import *
from user_action_decider.end_condition import *
import time
import json

goal = "Walk up to the pink cube. You can stop when within a few feet of it."

time.sleep(2)

ending = False

while not ending:
    counter = 0

    # screenshot
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

print("Done")
hold_key("right", 10)
