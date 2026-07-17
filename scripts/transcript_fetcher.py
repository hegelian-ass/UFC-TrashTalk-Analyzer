from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import os

INPUT_FILE = "data/video_ids.csv"
OUTPUT_FILE = "data/transcript_dataset.csv"
FAILED_FILE = "data/failed_videos.csv"

os.makedirs("data", exist_ok=True)

df = pd.read_csv(INPUT_FILE)

api = YouTubeTranscriptApi()

results = []
failed = []

for index, row in df.iterrows():
    video_id = row["video_id"]
    fighter = row["fighter"]

    try:
        transcript = api.fetch(video_id)

        full_text = " ".join([item.text for item in transcript])

        results.append({
            "fighter": fighter,
            "video_id": video_id,
            "transcript": full_text,
            "word_count": len(full_text.split())
        })

        print(f"Fetched: {video_id}")

    except Exception as e:
        failed.append({
            "fighter": fighter,
            "video_id": video_id,
            "error": str(e)
        })

        print(f"Failed: {video_id}")

    if (index + 1) % 50 == 0:
        pd.DataFrame(results).to_csv(OUTPUT_FILE, index=False)
        pd.DataFrame(failed).to_csv(FAILED_FILE, index=False)
        print(f"Checkpoint saved after {index + 1} videos")

pd.DataFrame(results).to_csv(OUTPUT_FILE, index=False)
pd.DataFrame(failed).to_csv(FAILED_FILE, index=False)

print("Transcript fetching completed.")