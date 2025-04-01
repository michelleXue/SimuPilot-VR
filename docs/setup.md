# Setup & Usage

## 1. Installation

```bash
git clone https://github.com/your-org/your-tool.git
cd your-tool
pip install -r requirements.txt

```
## Setup

(think about the hardware and software requirement to run the tool)

1. Ensure requirements are installed from requirements.txt

2. Install any VR display on computer. This includes software that mirrors the headset such as Meta's Air Link. For development, this project utilized the Meta XR simulator through Unity. As long as a portion of the computer screen is the VR view the tool will work.

## Usage

1. Set up bounds for screenshots. Using the bounds.py function, determine the pixel locations of the VR application on your screen. Place these bounds into the region variable.

2. Specify the quest/goal that you want the AI to accomplish by typing it as a message into the goal variable.

3. Provide a GPT API key by pasting one into api_key_txt.

4. When fully setup simply start the program.