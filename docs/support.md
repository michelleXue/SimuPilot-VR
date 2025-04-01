# Supported Functions

SimuPilot VR provides a range of built-in action functions that can be invoked by the LLM pilot or user interactions. These functions enable seamless control, intelligent automation, and contextual assistance inside VR applications.

---

## 🔢 Core Action Functions

| Function Name       | Description                                                | Parameters            | Example Usage                         |
|---------------------|------------------------------------------------------------|-----------------------|----------------------------------------|
| `move_forward()`    | Walks forward by pressing w key for a specified time       | `duration: float`     | `move_forward(2.0)`                    |
| `move_left()`    | Walks left by pressing a key for a specified time       | `duration: float`     | `move_left(2.5)`                    |
| `move_right()`    | Walks right by pressing d key for a specified time       | `duration: float`     | `move_right(1.5)`                    |
| `in_place_rotate_to_left()`    | Rotates to the left by the left arrow key for a specified time       | `duration: float`     | `in_place_rotate_to_left(0.5)`                    |
| `in_place_rotate_to_right()`   | Rotates to the left by the left arrow key for a specified time         | `duration: float`     | `in_place_rotate_to_right(0.5)`                    |

---

## 🔧 System & Utility Functions

| Function Name    | Description                                    | Parameters           | Example Usage                         |
|------------------|------------------------------------------------|-----------------------|----------------------------------------|
| `screenshot()`       | Captures a screenshot of the simulator screen     | `counter: int, region: int tuple, end: boolean` | `screenshot(3, (10, 10 5, 5), True)`  |
| ` compress_images_in_folder()`    | Compresses screenshot for AI to views             | `input_folder: str, output_folder: str, target_size: int`     | `compress_images_in_folder("temp/screenshot_original", "temp/screenshot_compressed", 512)`          |
| `detect_objects()` | AI determines what objects are in view and writes data to a json, returns object believed to be the target | `image_path: str, goal: str`          | `detect_objects("temp/screenshot_compressed", "reach the purple cube")`     |
| `determine_action()`  | Determines what action should be taken with AI              | `json_string: str, target: str`                  | `determine_action("json data", "purple-cube")`            |
| `finished()`  | Determines if the goal has been accomplished           | `goal: str, image_path: str`                  | `finished("reach cube", "temp/end_screenshots")`            |

---

For a full list of developer APIs and integration options, visit the [GitHub repository](https://github.com/your-org/your-tool).

