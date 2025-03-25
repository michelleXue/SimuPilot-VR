from user_action_decider.actions import *
from openai import OpenAI
from pydantic import BaseModel

with open("api_key.txt", "r") as file:
    key = file.read()

client = OpenAI(api_key=key)


class actionFormat(BaseModel):
    action: str
    duration: float


def determine_action(desc, target):
    response2 = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"The target you must reach is: {target}. To do this you can choose from the following actions: move_forward, move_left, move_right, in_place_rotate_to_left, in_place_rotate_to_right, and press. You must choose an action and how long you want to perform the action for. For example, you could say move_left 2.5 to move left for 2.5 seconds. Once your action is complete, you will get another image to continue from there. Be careful not to walk off the edge. The sensitivity is high, so when looking left or right do it in small increments. If you don't see the target try looking around slowly. Now what is your first action.",
                # look up down taken out
            },
            {"role": "user", "content": desc},
        ],
        response_format=actionFormat,
        max_tokens=300,
    )

    output = response2.choices[0].message

    if not output.refusal:
        print(output.parsed)

        dur = output.parsed.duration
        match output.parsed.action:
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
    else:
        print(output.refusal)
