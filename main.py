from user_action_decider.object_detection2 import *
from user_action_decider.actions import *
from user_action_decider.utils import *
from user_action_decider.json_action import *
import time
import json

api_key = ""

goal = "walk up to the table with buttons on it"

# screenshot
time.sleep(3)
screenshot(4)

# compress screenshot
compress_images_in_folder("temp/screenshot_original", "temp/screenshot_compressed")

# detect objects and save to json
detect_objects("temp/screenshot_compressed/screenshot4.png")

# parse json
jsonPath = "screenshotjson"

with open(jsonPath, "r", encoding="utf-8") as file:
    data = json.load(file)
    json_string = json.dumps(data)

# determine action
determine_action(data, goal)
