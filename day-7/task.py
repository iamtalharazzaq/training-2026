import requests
import json
import os
from collections import Counter
from datetime import datetime, timezone
import argparse

# Stopwords to exclude
STOPWORDS = {"the", "a", "an", "to", "of", "in", "and", "on", "for", "with", "at", "by", "is", "it"}

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Analyze top Reddit posts from a subreddit")
parser.add_argument("--subreddit", type=str, default="technology", help="Subreddit name (default: technology)")
args = parser.parse_args()

# Reddit API URL
URL = f"https://reddit.com/r/{args.subreddit}/top.json?limit=50"
headers = {"User-Agent": "Day7RedditAnalysisBot/0.1 by Talha"}

# Fetch data
response = requests.get(URL, headers=headers)
if response.status_code != 200:
    print(f"Error fetching data: {response.status_code}")
    exit()

data = response.json()["data"]["children"]

# Initialize analysis variables
titles = [post["data"]["title"] for post in data]
upvotes = [post["data"]["ups"] for post in data]
most_upvoted_post = max(data, key=lambda p: p["data"]["ups"])["data"]
today_count = 0
older_count = 0
word_counter = Counter()

# Current date in UTC
today = datetime.now(timezone.utc).date()

# Analyze posts
for post in data:
    post_data = post["data"]
    # Word frequency
    for word in post_data["title"].split():
        word_lower = word.lower().strip(".,!?\"'()[]{}")
        if word_lower and word_lower not in STOPWORDS:
            word_counter[word_lower] += 1
    # Date analysis
    post_date = datetime.fromtimestamp(post_data["created_utc"], tz=timezone.utc).date()
    if post_date == today:
        today_count += 1
    else:
        older_count += 1

# Top 20 words
top_words = word_counter.most_common(20)
avg_upvotes = sum(upvotes) / len(upvotes) if upvotes else 0

# Prepare report
report = {
    "subreddit": args.subreddit,
    "top_words": top_words,
    "most_upvoted_post": {
        "title": most_upvoted_post["title"],
        "upvotes": most_upvoted_post["ups"],
        "url": f"https://reddit.com{most_upvoted_post['permalink']}"
    },
    "average_upvotes": avg_upvotes,
    "posts_count": {
        "today": today_count,
        "older": older_count
    }
}

# Save report in the same folder as the script
current_dir = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(current_dir, "report.json")
with open(report_path, "w") as f:
    json.dump(report, f, indent=2)

# Print structured output
print("="*60)
print(f"REDDIT TOP 50 POSTS ANALYSIS: r/{args.subreddit}".center(60))
print("="*60)

print("\nTOP 20 WORDS IN TITLES:")
print("-"*60)
for i, (word, count) in enumerate(top_words, start=1):
    print(f"{i:2}. {word:<15} | Count: {count}")

print("\nMOST UPVOTED POST:")
print("-"*60)
print(f"Title   : {most_upvoted_post['title']}")
print(f"Upvotes : {most_upvoted_post['ups']}")
print(f"URL     : https://reddit.com{most_upvoted_post['permalink']}")

print("\nPOST STATISTICS:")
print("-"*60)
print(f"Average upvotes       : {avg_upvotes:.2f}")
print(f"Posts from today      : {today_count}")
print(f"Posts older than today: {older_count}")

print(f"\nReport saved to {report_path}")
print("="*60)