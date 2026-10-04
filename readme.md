# 🍳 RecipeVision AI

A simple multimodal AI agent that takes a **photo of ingredients** and generates a recipe using **LangChain, OpenAI, and Tavily**.

## Features

- 📸 Select an image of ingredients
- 👁️ Analyze ingredients with a vision-capable model
- 🤖 Use a LangChain agent to generate a recipe
- 🔎 Search the web with Tavily when recipe information is needed
- 🛠️ Use a custom `search_recipes` tool
- 💬 Send the image and instructions as a multimodal message

## How It Works

```text
📸 Ingredient Photo
        ↓
choose_image_file()
        ↓
build_image_message()
        ↓
HumanMessage
(text + image)
        ↓
🤖 LangChain Agent
        ↓
   ┌────┴────┐
   ↓         ↓
Analyze    search_recipes
Image          ↓
           Tavily Search
   └────┬────┘
        ↓
🍳 Final Recipe
```

## Tech Stack

- **Python**
- **LangChain**
- **OpenAI GPT-5-nano**
- **Tavily**
- **python-dotenv**

## Project Structure

```text
RecipeVisionAgent/
│
├── main.py
├── photo_decode.py
├── prompt.py
├── tools.py
├── pyproject.toml
├── uv.lock
├── .env
└── README.md
```

### Files

| File | Purpose |
|---|---|
| `main.py` | Creates and runs the LangChain agent |
| `photo_decode.py` | Selects the image and creates the multimodal message |
| `prompt.py` | Contains the chef prompts |
| `tools.py` | Contains the recipe search tool using Tavily |
| `.env` | Stores API keys |

## Setup

### 1. Clone the project

```bash
git clone <YOUR_REPOSITORY_URL>
cd RecipeVisionAgent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If you are using `uv`:

```bash
uv sync
```

### 4. Add API keys

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

The application loads these variables with:

```python
from dotenv import load_dotenv

load_dotenv()
```

### 5. Run

```bash
python main.py
```

Select an ingredient image when prompted.

## LangChain Agent

The agent is created with the model, recipe-search tool, and system prompt:

```python
agent = create_agent(
    model="gpt-5-nano",
    tools=[search_recipes],
    system_prompt=SYSTEM_CHEF_PROMPT
)
```

The ingredient image is converted into a multimodal message:

```python
path = choose_image_file()

message = build_image_message(
    path,
    CHEF_PROMPT
)
```

The message is passed to the agent:

```python
response = agent.invoke({
    "messages": [message]
})
```

The agent can analyze the image and decide whether it needs to call `search_recipes`.

## Tool Usage

The agent has access to:

```python
tools=[search_recipes]
```

The tool uses Tavily to search for recipe information.

```text
Agent
  ↓
search_recipes(query)
  ↓
Tavily
  ↓
Search results
  ↓
Agent
  ↓
Final recipe
```

This allows the agent to decide when web search is useful instead of always performing a search.

## Example

If the image contains:

```text
🥔 Potato
🍅 Tomato
🧅 Onion
🧄 Garlic
🌶️ Green Chili
```

The agent can identify the ingredients, search for relevant recipe information when required, and return a recipe with ingredients and cooking instructions.

## Security

Do not commit your API keys.

Add this to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

Never upload:

```text
OPENAI_API_KEY
TAVILY_API_KEY
```

to GitHub.

## Troubleshooting

### `ModuleNotFoundError: No module named 'photo_decode'`

Make sure the file is named:

```text
photo_decode.py
```

and not:

```text
photo-decode.py
```

### `Unsupported message type: <class 'set'>`

Use:

```python
response = agent.invoke({
    "messages": [message]
})
```

Do not use:

```python
{
    "messages": {
        "HumanMessage"
    }
}
```

The latter creates a Python `set`.

### `NameError: name 'logger' is not defined`

If `tools.py` contains:

```python
logger.info(...)
```

define the logger:

```python
import logging

logger = logging.getLogger(__name__)
```

## Future Improvements

- Direct camera capture
- Web interface
- Nutrition information
- Ingredient substitutions
- Grocery-list generation
- Dietary preferences
- Recipe history

## Author

**Sahil**

Built with Python, LangChain, OpenAI, and Tavily.
