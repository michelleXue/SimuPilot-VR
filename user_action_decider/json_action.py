from user_action_decider.actions import *
from openai import OpenAI
from pydantic import BaseModel
import main

client = OpenAI(main.api_key)


class actionFormat(BaseModel):
    action: str
    duration: float


def determine_action(desc):
    response2 = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "Your goal is to walk up to the table with the buttons on it. To do this you can choose from the following actions: move_forward, move_left, move_right, in_place_rotate_to_left, in_place_rotate_to_right, look_down, look_up, and press. You must choose an action and how long you want to perform the action for. For example, you could say move_left 2.5 to move left for 2.5 seconds. Once your action is complete, you will get another image to continue from there. Be careful not to walk off the edge. When you think you are there say stop 0. Now what is your first a action.",
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
        dur = 0.5
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
