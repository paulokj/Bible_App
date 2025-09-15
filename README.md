# 📖 Bible App

A simple **Bible Study App** built with [Streamlit](https://streamlit.io/), featuring **verse search** and **basic NLP-powered text analysis**.  

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bibleapp-9cg7hlsdpkzptrpkp7abya.streamlit.app/)


---

## 🎯 Aim
- Build a simple app with Streamlit for Bible Studies  
- Enable searching for **single verses** or **multiple verses**  
- Provide a **study mode** with text analysis (sentiment, keywords, word frequency, etc.)  

---

## 🗂️ App Structure
- 📍 **Single Verse Section** → search and retrieve one verse  
- 📚 **Multiple Verse Section** → retrieve multiple verses at once  
- 🔎 **Study Mode**  
  - Text analysis (basic NLP tools applied to selected verses)  

---

## 🛠️ Tech Stack & Packages

- [streamlit](https://streamlit.io/) – app framework  
- [pandas](https://pandas.pydata.org/) – data handling  
- [spaCy](https://spacy.io/) – NLP  
- [TextBlob](https://textblob.readthedocs.io/) – sentiment analysis  
- [neattext](https://pypi.org/project/neattext/) – text preprocessing  
- [NLTK](https://www.nltk.org/) – natural language toolkit  
- [Altair](https://altair-viz.github.io/) – plotting  
- [Matplotlib](https://matplotlib.org/) – plotting  

---

## 💻 Installation & Run

Clone the repo and install dependencies:

```bash
git clone https://github.com/paulokj/Bible_App.git
cd Bible_App
pip install -r requirements.txt
