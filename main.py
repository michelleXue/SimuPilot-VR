from user_action_decider.object_detection import *
from user_action_decider.actions import *
from user_action_decider.utils import *
from user_action_decider.json_action import *
from user_action_decider.end_condition import *
import json

# SimuPilot VR

# Setup:
# Set screenshot bounds with bounds.py and place region variable
# Set goal in goal variable
# Place api key in api_key.txt

goal = ""
region = (x1, y1, width, height)

ending = False

counter = 0

while not ending:

    # screenshot
    screenshot(counter, region)

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
    screenshot(counter, region, True)
    compress_images_in_folder("temp/screenshot_original", "temp/screenshot_compressed")
    ending = finished(goal, f"temp/screenshot_compressed/screenshotend{counter}.png")
    print(f"Finished: {ending}")

    counter += 1

print("Done")
