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