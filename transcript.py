import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url: str) -> str:
    """
    Extract YouTube video ID from URL.
    Supports normal, short, and shorts URLs.
    """
    # Normal URL
    match = re.search(r"v=([^&]+)", url)
    if match:
        return match.group(1)
    
    # Short URL
    match = re.search(r"youtu\.be/([^?&]+)", url)
    if match:
        return match.group(1)
    
    # Shorts URL
    match = re.search(r"shorts/([^?&]+)", url)
    if match:
        return match.group(1)
    
    raise ValueError("Invalid YouTube URL or unable to extract video ID")

def fetch_transcript_from_youtube(url: str) -> str:
    video_id = get_video_id(url)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = " ".join(item['text'] for item in transcript_list)
    return transcript
