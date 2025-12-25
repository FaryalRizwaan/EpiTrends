# EpiTrends 📊

**Real-time Public Health Trend Analyzer**

EpiTrends is a Python-based application designed to fetch, summarize, and analyze public health trends from **official sources like WHO and CDC**. It provides trend status, article counts, and headline summaries for health-related topics, assisting researchers, students, and healthcare professionals with **educational insights**.

---

## Features ✨

* Fetches health news from official RSS feeds (WHO, CDC)
* Summarizes articles for topics like **vaccination, COVID-19, flu, mental health, maternal health**
* Trend detection: Trending, Moderate, or Low activity
* FastAPI backend with easy-to-use endpoints
* Expandable keywords for broader topic coverage
* Educational and non-medical guidance only

---

## Tech Stack 🛠️

* **Python 3.10+**
* **FastAPI** – Backend API
* **Uvicorn** – ASGI server
* **Feedparser** – RSS feed processing
* **Streamlit** – Optional frontend for interactive dashboards
* **Git & GitHub** – Version control
* **Virtual Environment (.venv)** – Local dependency isolation

---

## Setup Guide 🚀

### 1. Clone the repository

Open your terminal in VS Code (or any terminal) and run:

```bash
git clone https://github.com/FaryalRizwaan/EpiTrends.git
cd EpiTrends
```

---

### 2. Setup a Python virtual environment

Create a `.venv` to isolate dependencies:

```bash
python -m venv .venv
```

Activate it:

* **Windows:**

```bash
.venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> This ensures all libraries like FastAPI, Uvicorn, Feedparser are installed.

---

### 4. Run the backend server

```bash
uvicorn backend:app --reload --host 0.0.0.0 --port 5000
```

* Access API locally at: `http://127.0.0.1:5000`
* Endpoint: `/generate-news-summary` accepts POST requests with JSON payload.

---

### 5. Example API Request

**POST** `http://127.0.0.1:5000/generate-news-summary`

```json
{
  "topics": ["vaccination", "covid"],
  "source_type": "news"
}
```

**Response:**

* Summaries per topic
* Article counts
* Trend status

---

### 6. Optional: Frontend with Streamlit

If you want an interactive dashboard:

```bash
streamlit run frontend.py
```

* Open in browser: `http://localhost:8501`
* Sidebar lets you select topics and source types

---

## Best Practices ⚡

* **Do not commit `.venv`** to GitHub – it is ignored via `.gitignore`
* Use `git pull origin main` to sync latest updates
* Handle CRLF/LF warnings in Windows:

```bash
git config --global core.autocrlf true
```

---

## Contributing 🤝

1. Fork the repository
2. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes:

```bash
git commit -m "Add feature X"
```

4. Push and create a pull request



## License 📄

MIT License – Free to use and modify for educational purposes.
