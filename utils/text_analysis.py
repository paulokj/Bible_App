# Core pkgs
import streamlit as st
import streamlit.components.v1 as stc


# analysis pkg
import pandas as pd

import re

# Viz pkgs
import altair as alt 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# NLP Pkgs
from textblob import TextBlob
import spacy
from spacy import displacy
from collections import Counter
from wordcloud import WordCloud


# --- SpaCy setup ---
# Load the small English model
# try:
#     # nlp = spacy.load('en_core_web_sm')
# except OSError:
#     # This should no longer happen in a properly deployed environment
#     # where the model is installed from requirements.txt
#     st.error("SpaCy model 'en_core_web_sm' not found.")
#     st.stop()

# Design
from utils.template import HTML_WRAPPER, HTML_BANNER

def plot_mendelhall_curve(docx):
	word_length = [ len(token) for token in docx.split()]
	word_length_count = Counter(word_length)
	sorted_word_length_count = sorted(dict(word_length_count).items())
	x,y = zip(*sorted_word_length_count)
	fig = plt.figure(figsize=(20,10))
	plt.plot(x,y)
	plt.title("Plot of Word Length Distribution")
	plt.show()
	st.pyplot(fig)


def get_tags(docx):
    tagged_docx = TextBlob(docx).tags
    return tagged_docx

TAGS = {
    'NN': 'green',
    'NNS': 'green',
    'NNP': 'green',
    'NNPS': 'green',
    'VB': 'blue',
    'VBD': 'blue',
    'VBG': 'blue',
    'VBN': 'blue',
    'VBP': 'blue',
    'VBZ': 'blue',
    'JJ': 'red',
    'JJR': 'red',
    'JJS': 'red',
    'RB': '#00FFFF',  # Cyan
    'RBR': '#00FFFF',
    'RBS': '#00FFFF',
    'IN': '#A9A9A9',  # DarkGray
    'POS': '#FFD700', # Gold (close to darkyellow)
    'PRP$': '#FF00FF',# Magenta
    'DET': '#000000', # Black
    'CC': '#000000',
    'CD': '#000000',
    'WDT': '#000000',
    'WP': '#000000',
    'WP$': '#000000',
    'WRB': '#000000',
    'EX': 'yellow',
    'FW': 'yellow',
    'LS': 'yellow',
    'MD': 'yellow',
    'PDT': 'yellow',
    'RP': 'yellow',
    'SYM': 'yellow',
    'TO': 'yellow',
    'None': 'transparent' # Or any valid color to hide
}

def mytag_visualizer(tagged_docx):
    """
    Applies color-coding to a list of tokens based on their POS tags.
    """
    colored_text = []
    for token, tag in tagged_docx:
        color_for_tag = TAGS.get(tag, 'transparent') # Use .get with a default value
        result = f'<span style="color:{color_for_tag}">{token}</span>'
        colored_text.append(result)
    
    return ' '.join(colored_text)


# def render_entities(raw_text):
#     """
#     Renders named entities from text using spaCy and displaCy.
#     """
#     docx = nlp(raw_text)
#     html = displacy.render(docx, style='ent', page=False)
#     result = HTML_WRAPPER.format(html)
#     stc.html(result, height=1000, scrolling=True)

def plot_most_common_tokens(docx, num=10):
    # This regular expression splits the text into words and also handles punctuation
    # It ensures that words are treated as a single token, e.g., "word." becomes "word"
    words = re.findall(r'\b\w+\b', docx.lower())
    
    word_freq = Counter(words)
    most_common_tokens = word_freq.most_common(num)

    if not most_common_tokens:
        st.write("No tokens to display.")
        return

    x, y = zip(*most_common_tokens)
    
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(x, y)
    ax.set_title("Most Common Tokens")
    plt.xticks(rotation=45)
    
    st.pyplot(fig)

def plot_word_freq_with_altair(docx,num=10):
	word_freq = Counter(docx.split())
	most_common_tokens = dict(word_freq.most_common(num))
	word_freq_df = pd.DataFrame({'tokens':most_common_tokens.keys(),'counts':most_common_tokens.values()})
	c = alt.Chart(word_freq_df).mark_bar().encode(
		x='tokens',y='counts')
	st.altair_chart(c,use_container_width=True)
     
def plot_tags_value_count(docx):
     tagged_docx = get_tags(docx)
     tagged_df = pd.DataFrame(tagged_docx, columns=['Tokens', 'Tags'])
    #  st.dataframe(tagged_df)
     df_tag_count = tagged_df['Tags'].value_counts().to_frame('counts')
     df_tag_count['tag_type'] = df_tag_count.index
    #  st.dataframe(df_tag_count)
     c = alt.Chart(df_tag_count).mark_bar().encode(x='tag_type', y='counts')
     st.altair_chart(c)

def render_word_cloud(raw_text):
    """
    Generates and renders a word frequency cloud from the text.
    """
    if not raw_text:
        return
        
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(raw_text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)