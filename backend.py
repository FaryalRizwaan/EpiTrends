from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import feedparser

# -----------------------------
# Request Model
# -----------------------------

HEALTH_KEYWORDS = {
    "vaccination": [
        "vaccination", "immunization", "vaccine rollout",
        "public health vaccination", "WHO vaccination"
    ],
    "covid": [
        "covid", "covid-19", "coronavirus",
        "WHO covid update", "public health covid"
    ],
    "flu": [
        "influenza", "seasonal flu", "flu outbreak",
        "public health flu"
    ],
    "mental health": [
        "mental health", "depression", "anxiety",
        "WHO mental health", "public mental health"
    ],
    "maternal health": [
        "maternal health", "pregnancy care",
        "WHO maternal health", "childbirth safety"
    ]
}

class NewsSummaryRequest(BaseModel):
    topics: list[str]
    source_type: str  # "news" or "both"

# -----------------------------
# App Init
# -----------------------------
app = FastAPI(title="HealthTrendAnalyzer Backend")

# -----------------------------
# RSS Feeds
# -----------------------------
RSS_FEEDS = {
    "WHO": "https://www.who.int/rss-feeds/news-english.xml",
    "CDC": "https://www.cdc.gov/rss/rss.xml"
}

# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/generate-news-summary")
def generate_news_summary(request: NewsSummaryRequest):
    if not request.topics:
        raise HTTPException(status_code=400, detail="No topics provided")

    summaries = {}

    for topic in request.topics:
        summaries[topic] = generate_summary(topic)

    return {
    "status": "success",
    "summaries": summaries,
    "counts": {
        topic: len(fetch_news(topic))
        for topic in request.topics
    }
}


# -----------------------------
# Core Logic
# -----------------------------
def generate_summary(topic: str) -> str:
    articles = fetch_news(topic)
    count = len(articles)

    trend_label = determine_trend(count)

    summary = f"""
**Topic:** {topic}

**Articles found:** {count}  
**Trend status:** {trend_label}

**What recent headlines indicate:**
"""

    if articles:
        for title, link in articles[:5]:
            summary += f"- {title}\n"
    else:
        summary += "- No recent official headlines found.\n"

    summary += (
        "\n*Note: Summaries are based on official public health headlines "
        "and do not include full article content.*"
    )

    return summary.strip()

# -----------------------------
# Fetch RSS News
# -----------------------------
def fetch_news(topic: str):
    keywords = HEALTH_KEYWORDS.get(topic.lower(), [topic.lower()])
    articles = []

    for source, feed_url in RSS_FEEDS.items():
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            title = entry.get("title", "").lower()
            summary = entry.get("summary", "").lower()

            if any(kw.lower() in title or kw.lower() in summary for kw in keywords):
                articles.append((entry.title, entry.link))

    return articles

# -----------------------------
# Trend Classification
# -----------------------------
def determine_trend(count: int) -> str:
    if count >= 7:
        return "Trending 🔼"
    elif count >= 3:
        return "Moderate activity"
    else:
        return "Low activity"

# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
