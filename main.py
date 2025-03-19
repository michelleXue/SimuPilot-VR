from user_action_decider.object_detection import *
from user_action_decider.actions import *
from user_action_decider.utils import *
from user_action_decider.json_action import *
import time
import json

goal = "walk up to the purple cube"

while True:
    counter = 0

    # screenshot
    # time.sleep(2)
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
