from user_action_decider.actions import *
from openai import OpenAI
from pydantic import BaseModel

from user_action_decider.utils import encode_image

with open("api_key.txt", "r") as file:
    key = file.read()

client = OpenAI(api_key=key)


class end(BaseModel):
    accomplished: bool


def finished(goal, path):
    base64_image = encode_image(path)

    end_condition = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are using a virtual reality assistant and this image is what you are seeing.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Your goal was: {goal}, have you accomplished this goal based on this image of what you are seeing?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            },
        ],
        response_format=end,
        max_tokens=500,
    )

    output = end_condition.choices[0].message
    return output.parsed.accomplished
