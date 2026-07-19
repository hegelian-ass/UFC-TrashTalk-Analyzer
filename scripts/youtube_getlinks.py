import pandas as pd
import os
import requests

API_KEY = "YOUR_API_KEY"

OUTPUT_FILE = "data/video_ids.csv"

SEARCH_QUERIES = [
    "press conference",
    "pre fight interview",
    "media day"
]

url = "https://www.googleapis.com/youtube/v3/search"
results = []

fighter = input("Enter fighter name: ")
for search_query in SEARCH_QUERIES:
    search_term = fighter + " " + search_query
    params = {
    "key": API_KEY,
    "q": search_term,
    "part": "snippet",
    "type": "video",
    "maxResults": 50
    }
    response = requests.get(url, params=params)
data = response.json()

items = data["items"]

for item in items:
    video_id = item["id"]["videoId"]
    title = item["snippet"]["title"]
    channel = item["snippet"]["channelTitle"]
    published_at = item["snippet"]["publishedAt"]
    extract = {
    "fighter": fighter,
    "video_id": video_id,
    "title": title,
    "channel": channel,
    "published_at": published_at,
    "search_query": search_query
}

results.append(extract)
print(results[-1])