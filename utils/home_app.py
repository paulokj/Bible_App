# Core pkg
import streamlit as st
import streamlit.components.v1 as stc

# EDA
import pandas as pd
import random

# Design 
from utils.template import HTML_RANDOM_TEMPLATE

# Bible loader
from data.bible_loader import load_bible

def home_page():
    st.subheader("Single Verse Search")
    df = load_bible('data/KJV_Bible.csv')
    # st.dataframe(df)

    # booklist sidebar
    book_list = df['book'].unique().tolist()
    book_name = st.sidebar.selectbox("Book", book_list)

    # chapter sidebar
    min_book_chapter = int((df['chapter'][df['book'] == book_name]).min())
    max_book_chapter = int((df['chapter'][df['book'] == book_name]).max())
    # st.write(max_book_chapter)
    chapter = st.sidebar.number_input("Chapter", min_book_chapter, max_book_chapter)

    # verse sidebar
    min_verse = int((df['verse'][(df['book'] == book_name) & (df['chapter'] == chapter)]).min())
    max_verse = int((df['verse'][(df['book'] == book_name) & (df['chapter'] == chapter)]).max())
    verse = st.sidebar.number_input("Verse", min_verse, max_verse)

    #Layout
    c1,c2 = st.columns([2, 1])

    # Single Verse
    with c1:
        try:
            # Displaying only selected - Book, Chaper and Verse
            selected_passage = df[(df['book'] == book_name) & (df['chapter'] == chapter) & (df['verse'] == verse)]
            # st.write(selected_passage['text'].values[0])
            passage_details = "{} {}: {}".format(book_name, chapter, verse)
            st.info(passage_details)
            passage = "{}".format(selected_passage['text'].values[0])
            st.write(passage)
        except:
            st.warning("Book/verse out of range")
    with c2:
        st.success('Verse of the day')
        # Pick random book
        random_book = random.choice(book_list)

        # Get valid chapter range from select book
        chapters = df[df['book'] == random_book]['chapter'].unique()
        chapter_choice = random.choice(chapters)

        # Get valid verse range for that chapter
        verses = df[(df['book'] == random_book) & (df['chapter'] == chapter_choice)]['verse'].unique()
        verse_choice = random.choice(verses)
        
        st.write(f'{random_book} {chapter_choice} : {verse_choice}')
        try:
            # Displaying only selected - Book, Chaper and Verse
            selected_random_passage = df[(df['book'] == random_book) & (df['chapter'] == chapter_choice) & (df['verse'] == verse_choice)]
            # st.write(selected_random_passage['text'].values[0])
            stc.html(HTML_RANDOM_TEMPLATE.format(selected_random_passage['text'].values[0]),
                     height = 300, scrolling = True)
        except:
            st.warning('Unable to retrieve a verse today')


    # Search Topic / Term
    search_term = st.text_input("Term / Topic")
    if st.button('Search'):
        with st.expander('View Results'):
            retrieved_df = df[df['text'].str.contains(search_term)]
            st.dataframe(retrieved_df[['book', 'chapter', 'verse', 'text']])
