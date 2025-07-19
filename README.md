# ClipGPT: Summarize and Tag YouTube Shorts Using LLMs

ClipGPT is a simple Python tool that takes a YouTube Short video URL, extracts the transcript, and uses an OpenAI GPT model to generate a summary, hashtags, and a viral-style title.

---

## Features

- Extracts transcript from YouTube videos using `youtube-transcript-api`
- Uses OpenAI GPT-4 Turbo for summarization and tagging
- CLI tool that accepts YouTube URLs as input

---

## Requirements

- Python 3.8 or higher
- An OpenAI API key (see setup below)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ClipGPT.git
cd ClipGPT
```

### 2. Create and activate a virtual environment (recommended)

- On Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

- On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Get Your OpenAI API Key

1. Sign up or log in at [OpenAI Platform](https://platform.openai.com/)
2. Navigate to **API Keys** in your account dashboard.
3. Create a new secret key and copy it.

---

## Provide Your API Key

There are two ways to provide your OpenAI API key:

### Option A: Set as environment variable (recommended)

- On Windows (PowerShell):

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

*Close and reopen your terminal after setting this.*

- On macOS/Linux:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Option B: Edit `prompt_engine.py`

Replace the line:

```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```

with

```python
openai.api_key = "your_api_key_here"
```

---

## How to Run

Run the tool from the command line by passing a YouTube video or Shorts URL as an argument:

```bash
python main.py https://www.youtube.com/shorts/dQw4w9WgXcQ
```

The program will:

- Fetch the video transcript
- Send it to the GPT model for summarization and tagging
- Print the result in your terminal

---

## Troubleshooting

- If transcript fetching fails, make sure the video has captions or is not restricted.
- Ensure your OpenAI API key is set correctly and has usage quota.
- For any errors, check your internet connection and dependencies.


---

Feel free to contribute or raise issues!
