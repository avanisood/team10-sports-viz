# 🏏 Sports Data Analysis & Visualization (Team 10)

### Domain: Sports
**Project Type:** Data Visualization & Text Analysis  
**Live Website:** [Insert your GitHub Pages Link Here]  
**Video Demo:** [Insert your YouTube Link Here]

---

## 📖 Project Overview
This project analyzes **500+ user prompts** related to sports (Cricket, Football, Chess, etc.) extracted from large open-source datasets (ShareGPT, Dolly-15k, OASST1). 

The goal was to understand **how humans interact with AI regarding sports**. We moved beyond simple counting to analyze:
* **User Intent:** Do fans want stats, rules, or gossip?
* **Psychology:** Are fans angry or analytical?
* **Linguistics:** How does the vocabulary differ between sports?

---

## 📊 Visualizations (The Dashboard)
We created 6 interactive visualizations hosted on a D3.js website:

1.  **The Flow of Curiosity (Sankey Diagram):** * *Insight:* Traces the user's journey from a Sport (Topic) to their Cognitive Goal (Who/What/How).
2.  **Fan vs. Analyst Quadrant (Sentiment Scatter Plot):**
    * *Insight:* Maps users on a "Psychological Grid" of Emotion vs. Subjectivity.
3.  **The Lexical Butterfly (Diverging Bar Chart):**
    * *Insight:* A side-by-side linguistic comparison showing unique vocabulary differences between Cricket and Football.
4.  **The Entity Galaxy (Bubble Chart):**
    * *Insight:* Highlights the most famous "Named Entities" (Players/Teams), showing which stars dominate the conversation.
5.  **Complexity Heatmap:**
    * *Insight:* A matrix showing which sports trigger long, complex essays vs. short, factual queries.
6.  **Word Chord Diagram:**
    * *Insight:* Visualizes the "Universal Language of Sports" by connecting domains that share common terminology.

---

## 🛠️ Technical Implementation

### 1. Data Extraction Pipeline (`filter_sports_strict_clean.py`)
We developed a custom Python script to mine prompts from massive JSONL/CSV datasets.
* **Source Datasets:** Databricks-Dolly-15k, ShareGPT, Awesome-ChatGPT-Prompts.
* **Filtering Logic:** Used **Strict Regex Matching** (`\bword\b`) to ensure precision (e.g., ensuring "Cricket" doesn't match "Crickets").
* **Data Cleaning:** Removed stopwords, handled encoding errors, and normalized text.

### 2. Analysis Stack
* **Python:** The core logic engine.
* **TextBlob:** For Sentiment (Polarity) and Subjectivity scoring.
* **Spacy (en_core_web_sm):** For Named Entity Recognition (NER) to find players and teams.
* **NetworkX:** For mapping word relationships.
* **Pandas:** For data structuring and manipulation.

### 3. Visualization Stack
* **D3.js:** Used for high-performance, interactive rendering on the web.
* **HTML5/CSS3:** For the dashboard layout and responsive design.

---

## 🚀 How to Run Locally

### Prerequisites
* Python 3.8+
* A modern web browser

### Step 1: Install Dependencies
```bash
pip install pandas textblob spacy networkx matplotlib
python -m spacy download en_core_web_sm

Team10_Project/
│
├── filter_sports_strict_clean.py  # Script to mine data from raw sources
├── clean_sports_data.csv          # The final processed dataset (500+ rows)
│
├── index.html                     # Main dashboard landing page
├── style.css                      # Styling for the dashboard
│
├── d3_sankey.html               # Individual visualization files...
├── d3_scatter.html
├── d3_network.html
├── d3_bubble.html
├── d3_heatmap.html
└── d3_chord.html