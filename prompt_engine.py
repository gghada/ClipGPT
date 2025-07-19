# prompt_engine.py
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_and_tag(transcript: str):
    prompt = f"""
You are a helpful assistant for social media video creators.
Here's a video transcript:
\"\"\"
{transcript}
\"\"\"

Tasks:
1. Give a short and engaging summary (max 3 sentences).
2. Suggest 3-5 hashtags.
3. Rewrite the title in a viral style.

Respond in this format:
Summary: ...
Hashtags: ...
Title: ...
"""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
