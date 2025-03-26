# Supported Functions

SimuPilot VR provides a range of built-in action functions that can be invoked by the LLM pilot or user interactions. These functions enable seamless control, intelligent automation, and contextual assistance inside VR applications.

---

## 🔢 Core Action Functions

| Function Name       | Description                                                | Parameters           | Example Usage                         |
|---------------------|------------------------------------------------------------|-----------------------|----------------------------------------|
| `start_simulation()`| Initializes and begins a VR simulation session             | None                  | Voice: "Begin the simulation"         |
| `pause_session()`   | Pauses the current VR session                              | None                  | Voice: "Pause now"                    |
| `load_scenario()`   | Loads a predefined scenario or environment                 | `scenario_id: str`    | Voice: "Load training level one"      |
| `highlight_object()`| Highlights an object for user attention                    | `object_id: str`      | Voice: "Show me the navigation panel" |
| `explain_feature()` | Provides verbal or textual explanation of a selected item | `feature_id: str`     | Voice: "What does this button do?"    |

---

## 🔧 System & Utility Functions

| Function Name    | Description                                    | Parameters           | Example Usage                         |
|------------------|------------------------------------------------|-----------------------|----------------------------------------|
| `bounds()`       | Cpature the bounds of the simulator screen     | `rating: int, notes: str` | Voice: "Give feedback: 4 stars"  |
| `toggle_ui()`    | Show/hide in-VR interface elements             | `element_id: str`     | Voice: "Hide the sidebar"             |
| `request_help()` | Asks for contextual help or triggers LLM query | `topic: str`          | Voice: "I need help with controls"     |
| `end_session()`  | Gracefully ends the VR session                 | None                  | Voice: "Exit simulation"              |

---

For a full list of developer APIs and integration options, visit the [GitHub repository](https://github.com/your-org/your-tool).

