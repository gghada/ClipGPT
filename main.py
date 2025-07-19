import argparse
from transcript import fetch_transcript_from_youtube
from prompt_engine import summarize_and_tag

def run_clipgpt(youtube_url):
    print("[+] Fetching transcript...")
    try:
        transcript = fetch_transcript_from_youtube(youtube_url)
    except Exception as e:
        print(f"[!] Error fetching transcript: {e}")
        return

    print("[+] Sending to LLM...")
    result = summarize_and_tag(transcript)

    print("\n📋 ClipGPT Result:\n")
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ClipGPT: Summarize and tag YouTube Shorts using LLMs")
    parser.add_argument("url", help="YouTube Shorts or video URL")

    args = parser.parse_args()
    run_clipgpt(args.url)
