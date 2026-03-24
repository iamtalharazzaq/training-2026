# Day 7: Reddit Data Analysis & JSON Reporting

This folder contains a Python script that interacts with the Reddit API to fetch and analyze top posts from a specified subreddit. It demonstrates advanced API interaction, data processing, and automated reporting.

---

## Exercise — `task.py` (Reddit Top Posts Analyzer)
- Fetches the top 50 posts from a subreddit (default: `technology`) using the Reddit JSON API.
- **Word Frequency Analysis**: Extracts words from all post titles, filters out common stopwords, and identifies the top 20 most frequent terms.
- **Upvote Statistics**: Calculates the average upvote count for the fetched posts.
- **Date Analysis**: Categorizes posts as either "today" or "older" based on their UTC creation timestamp.
- **JSON Reporting**: Automatically generates a `report.json` file containing the analysis results (top words, most upvoted post details, etc.).
- **Usage**:
  ```bash
  python3 task.py --subreddit <subreddit_name>
  # Example: python3 task.py --subreddit python
  ```

### Example Console Output:
```text
============================================================
      REDDIT TOP 50 POSTS ANALYSIS: r/technology       
============================================================

TOP 20 WORDS IN TITLES:
------------------------------------------------------------
 1. ai              | Count: 12
 2. google          | Count: 8
 3. apple           | Count: 5
 ...

MOST UPVOTED POST:
------------------------------------------------------------
Title   : Example Post Title
Upvotes : 54200
URL     : https://reddit.com/r/technology/comments/...

POST STATISTICS:
------------------------------------------------------------
Average upvotes       : 12450.32
Posts from today      : 15
Posts older than today: 35

Report saved to /home/ubuntu/projects/training-2026/day-7/report.json
============================================================
```

---

## Technical Skills Demonstrated:
1. **API Integration**: Using `requests` with custom `User-Agent` headers to satisfy Reddit's API requirements.
2. **Command-Line Arguments**: Implementing `argparse` for a flexible CLI interface.
3. **Data Processing**: Utilizing `collections.Counter` for efficient word frequency counts.
4. **Time Handling**: Converting UNIX timestamps to Python `datetime` objects with timezone awareness.
5. **JSON Management**: Serializing complex dictionaries into formatted JSON files using `json.dump()`.

---

## How to Run:
```bash
python3 task.py
```
