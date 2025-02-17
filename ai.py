from actions import *
from openai import OpenAI
import base64
from io import BytesIO
import time

time.sleep(1)
counter = 0
client = OpenAI(api_key="")

pressed = False

while not pressed:

    image = screenshot(counter)
    counter += 1
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

    response1 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are using a virtual reality assistant and this image is what you are seeing.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Where is the table with buttons."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            },
        ],
        max_tokens=300,
    )

    print(response1.choices[0].message.content)

    response2 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are using a virtual reality assistant.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Your goal is to walk up to the table with the buttons on it. To do this you can choose from the following actions: move_forward, move_left, move_right, in_place_rotate_to_left, in_place_rotate_to_right, look_down, look_up, and press. You must choose an action and how long you want to perform the action for. For example, you could say move_left 2 to move left for 2 seconds. You must say your answer in that format, action space duration. Once your action is complete, you will get another image to continue from there. Be careful not to walk off the edge. When you think you are there say stop 0. Now what is your first a action.",
                    },
                    {"type": "text", "text": response1.choices[0].message.content},
                ],
            },
        ],
        max_tokens=300,
    )

    print(response2.choices[0].message.content)

    act, dur = response2.choices[0].message.content.split()
    dur = int(dur)

    match act:
        case "move_forward":
            move_forward(dur)
        case "move_left":
            move_left(dur)
        case "move_right":
            move_right(dur)
        case "in_place_rotate_to_left":
            in_place_rotate_to_left(dur)
        case "in_place_rotate_to_right":
            in_place_rotate_to_right(dur)
        case "look_down":
            look_down(dur)
        case "look_up":
            look_up(dur)
        case "press":
            press_button(dur)
        case "stop":
            pressed = True
