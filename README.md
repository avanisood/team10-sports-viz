# � Sports Data Analysis & Visualization (Team 10)

### Domain: Sports
**Project Type:** Data Visualization & Text Analysis  
**Dataset:** 520 user prompts across 4 sports (Basketball, Football, Cricket, Chess)  
**Live Website:** [Open team10_index.html]

---

## 📖 Project Overview
This project analyzes **520 user prompts** related to sports (Basketball, Football, Cricket, Chess) to understand **how humans interact with AI regarding sports topics**. 

We moved beyond simple counting to analyze:
* **User Intent:** Do fans want stats, rules, or player information?
* **Psychology:** What is the emotional tone and subjectivity of queries?
* **Linguistics:** How does vocabulary differ between sports?
* **Entity Recognition:** Which players, teams, and organizations dominate conversations?
* **Complexity Patterns:** Which sports trigger long-form discussions vs. short queries?

---

## 📊 Visualizations (6 Interactive D3.js Charts)

### 1. **The Flow of Curiosity (Sankey Diagram)**
- **Insight:** Traces how 520 user queries flow from sports topics to cognitive intent categories
- **Classification:** Who (People), How (Rules), When/What (Facts), General
- **File:** `d3_sankey.html`

### 2. **The Psychology of Sports Prompts (Sentiment Scatter Plot)**
- **Insight:** Maps queries on a 2D psychological grid (Sentiment vs. Subjectivity)
- **Method:** TextBlob sentiment analysis with quadrant clustering
- **Reveals:** Separates "analytical thinkers" from "passionate superfans"
- **File:** `d3_sentiment_scatter.html`

### 3. **Cricket vs Football: Word Usage Comparison (Diverging Bar Chart)**
- **Insight:** Linguistic showdown revealing vocabulary differences
- **Analysis:** Top 10 most frequent Cricket words compared with Football usage
- **File:** `d3_diverging_bar.html`

### 4. **The Entity Galaxy (Bubble Chart)**
- **Insight:** Named entities (players, teams, organizations) extracted via Spacy NER
- **Data:** 4,617 entities identified, with NBA (116), NFL (55), and India (45) at the top
- **Interactive:** Drag bubbles to reposition
- **File:** `d3_entity_bubble.html`

### 5. **Complexity Heatmap**
- **Insight:** Prompt length distribution by sport
- **Categories:** Short (<10 words), Medium (10-30), Long (30-60), Essay (60+)
- **Finding:** Football prompts are 60.7% long-form; Cricket 55.8%
- **File:** `d3_heatmap.html`

### 6. **Sports-Words Connection (Chord Diagram)**
- **Insight:** Visualizes shared vocabulary across all sports
- **Analysis:** 1,720 shared words identified
- **Visual:** Circular arcs represent sports; ribbons show word overlap
- **File:** `d3_chord.html`

---

## 🛠️ Technical Implementation

### Data Analysis Stack (Python Scripts - To Be Added)
* **Pandas:** Data manipulation and structuring
* **TextBlob:** Sentiment (Polarity) and Subjectivity scoring
* **Spacy (en_core_web_sm):** Named Entity Recognition (NER)
* **Plotly:** Initial prototyping of visualizations
* **Seaborn/Matplotlib:** Statistical visualizations
* **Regular Expressions:** Intent classification logic

### Visualization Stack
* **D3.js v7:** High-performance interactive visualizations
* **D3-Sankey Plugin:** Flow diagram rendering
* **HTML5/CSS3:** Responsive dashboard layout with glass-morphism design
* **Dark Theme:** Gradient backgrounds (#0f0c29 → #302b63 → #24243e)

### Key Features
* **Lightweight:** D3.js files are 5-8KB (99% smaller than Plotly alternatives)
* **Interactive:** Hover tooltips, drag-and-drop, zoom capabilities
* **Responsive:** Adaptive layouts for different screen sizes
* **Professional:** Publication-ready with comprehensive legends and axis labels

---

## 🚀 How to Run Locally

### Prerequisites
* A modern web browser (Chrome, Firefox, Safari, Edge)
* No server required - all files run client-side

### Step 1: Open the Dashboard
1. Navigate to the `project_2` folder
2. Open `team10_index.html` in your web browser
3. All 6 visualizations are embedded with preview thumbnails
4. Click "View Full Screen" on any visualization for detailed interaction

### Step 2: View Individual Visualizations
Each visualization can be opened independently:
```bash
# Open any D3 visualization directly in your browser
d3_sankey.html
d3_sentiment_scatter.html
d3_diverging_bar.html
d3_entity_bubble.html
d3_heatmap.html
d3_chord.html
```

**Note:** The Sankey and Sentiment Scatter visualizations require `clean_sports_data.csv` to be in the same directory.

---

## 📁 Project Structure

```
project_2/
│
├── team10_index.html              # Main landing page with all visualizations
├── clean_sports_data.csv          # Dataset: 520 sports prompts
│
├── d3_sankey.html                 # Visualization 1: Sankey Diagram
├── d3_sentiment_scatter.html      # Visualization 2: Sentiment Scatter Plot
├── d3_diverging_bar.html          # Visualization 3: Diverging Bar Chart
├── d3_entity_bubble.html          # Visualization 4: Entity Bubble Chart
├── d3_heatmap.html                # Visualization 5: Complexity Heatmap
├── d3_chord.html                  # Visualization 6: Chord Diagram
│
└── README.md                      # This file
```

---

## 📊 Dataset Details

**File:** `clean_sports_data.csv`  
**Total Prompts:** 520  
**Sports Distribution:**
- Football: 257 prompts (49.4%)
- Basketball: 127 prompts (24.4%)
- Cricket: 95 prompts (18.3%)
- Chess: 41 prompts (7.9%)

**Columns:**
- `Prompt_Text`: The user query text
- `Matched_Keyword`: Sport category (basketball, football, cricket, chess)

---

## 🎯 Key Insights Discovered

1. **Intent Patterns:** Football users focus on "Who" questions (player info), while Chess users prefer "How" questions (strategy)

2. **Sentiment Analysis:** Mean sentiment score of 0.141 (slightly positive), indicating generally neutral-to-positive tone

3. **Entity Dominance:** NBA appears 116 times, NFL 55 times, India 45 times - showing Western sports leagues and cricket's Indian connection

4. **Complexity:** 60.7% of Football prompts are long-form (60+ words), vs. only 22% for Chess - suggesting Football generates more detailed discussions

5. **Shared Vocabulary:** 1,720 words are common across all sports, forming a "universal sports language"

6. **Linguistic DNA:** Words like "wicket" (Cricket-only) vs. "offside" (Football-specific) create distinct sport identities

---

## 🏅 Team Information

**Team Name:** Team 10  
**Project:** Sports Data Analysis & Interactive Visualizations  
**Technologies:** Python, D3.js, HTML5, CSS3, NLP (TextBlob, Spacy)

---

## 📝 Future Enhancements

- [ ] Add Python analysis scripts to repository
- [ ] Implement real-time data updates
- [ ] Add more sports categories (Tennis, Baseball, etc.)
- [ ] Create downloadable reports
- [ ] Add data filtering controls to dashboard
- [ ] Deploy to GitHub Pages for online access

---

## 📄 License

This project is for educational purposes as part of a data visualization course.