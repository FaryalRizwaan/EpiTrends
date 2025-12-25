HealthTrendAnalyzer 🩺

Project Description 📘

HealthTrendAnalyzer is a professional, credible, and educational public health trend analysis platform built using FastAPI and Streamlit. The application aggregates official public health news sources, analyzes topic-level trends, and presents readable summaries and visual insights strictly for educational and research purposes.

Project Overview 🎯

The goal of HealthTrendAnalyzer is to help users explore public health trends such as vaccination, COVID-19, flu, mental health, and maternal health. It collects news from authoritative public health organizations, applies domain-aware keyword expansion for better coverage, classifies trends based on article volume, and presents summaries and visual charts in an interactive dashboard.

This application does not provide medical advice.

Key Features ✨

Use of official public health data sources such as the World Health Organization and the Centers for Disease Control and Prevention
Expanded keyword-based topic retrieval to improve news coverage
Clear trend classification including low, moderate, and trending activity
Human-readable summaries generated from official headlines
Interactive visual trend comparison charts
Ethical disclaimer for public health-related content
Clear separation of frontend and backend architecture

System Architecture 🏗️

The user interacts with a Streamlit-based frontend interface. The frontend sends requests to a FastAPI backend, which fetches and processes data from official RSS feeds provided by organizations such as WHO and CDC. The backend then returns structured summaries and trend indicators to the frontend.

Frontend Responsibilities 🖥️

Allow users to select up to four public health topics
Provide options for selecting data sources
Trigger summary generation requests
Display summaries and trend visualizations

Backend Responsibilities ⚙️

Validate incoming user requests
Aggregate RSS feeds from official public health sources
Apply expanded health-related keyword mappings
Count relevant articles per topic
Determine trend levels based on article volume

Data Sources 📰

This project intentionally avoids social media and unverified sources. It relies only on trusted and authoritative organizations to ensure accuracy, scientific credibility, and public health relevance.

World Health Organization
Centers for Disease Control and Prevention

Trend Classification Logic 📊

Topics with seven or more related articles are classified as Trending
Topics with three to six related articles are classified as Moderate Activity
Topics with fewer than three related articles are classified as Low Activity

This rule-based approach ensures transparent and explainable trend labeling.

Technology Stack 🧠

Frontend built with Streamlit
Backend built with FastAPI
RSS parsing handled using feedparser
Visualizations created using Streamlit charts and pandas
Server run using Uvicorn
Programming language Python version 3.10 or higher

Installation and Setup 🛠️

Clone the repository and navigate into the project directory. Create and activate a virtual environment, then install dependencies using the requirements file.

Running the Application ▶️

Start the backend server using python backend.py. The backend runs locally on port 5000.

Start the frontend dashboard using streamlit run frontend.py. The application opens in the browser.

Ethical Disclaimer ⚠️

This application provides public health trend summaries for educational and research purposes only. It does not offer medical advice, diagnosis, or treatment recommendations. Users should consult qualified healthcare professionals for medical decisions.

Data Ethics and Responsibility 🔐

No personal data is collected
No predictive or diagnostic health claims are made
No medical recommendations are generated
Only publicly available official information is used

Future Enhancements 🚀

Addition of UNICEF, NIH, and national health portals
Time-series trend comparison and visualization
Topic clustering and deeper analytics
Audio summaries for accessibility
API caching and performance optimization

Author 👩‍💻

Faryal
Public Health and Data Analytics Project

Project Significance 🌍

HealthTrendAnalyzer demonstrates real-world data engineering skills, ethical handling of health information, clean system design, and practical public health analytics suitable for academic evaluation and professional portfolios.
