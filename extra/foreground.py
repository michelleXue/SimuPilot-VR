from user_action_decider.actions import *
from openai import OpenAI
import base64
from io import BytesIO
import time
from pydantic import BaseModel

with open("api_key.txt", "r") as file:
    key = file.read()

client = OpenAI(api_key=key)


class Spatial(BaseModel):
    reached: bool


# # Load your image and encode it in base64
# image_path = "screenshot4.png"  # Update this with your image path
# with open(image_path, "rb") as image_file:
#     base64_image = base64.b64encode(image_file.read()).decode("utf-8")
image = screenshot(-1)
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
                {
                    "type": "text"
                    "Is the table with buttons on it within a human's reach, as in could a human reach their arm out and press the button?",
                },
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
