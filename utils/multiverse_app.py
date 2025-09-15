# Core pkg
import streamlit as st
import streamlit.components.v1 as stc

# EDA
import pandas as pd

# Bible loader
from data.bible_loader import load_bible

# Utils pkgs
from utils.template import HTML_WRAPPER

# EDA pkgs
import neattext.functions as nfx

# NLP analysis
from utils.text_analysis import ( get_tags, mytag_visualizer,
                                 plot_most_common_tokens, plot_mendelhall_curve,
                                 plot_word_freq_with_altair, plot_tags_value_count,
                                 render_word_cloud)

def multiverse_page():
    st.subheader("Multi Verse Retrieval")
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
    # max_verse = int((df['verse'][(df['book'] == book_name) & (df['chapter'] == chapter)]).max())
    # verse = st.sidebar.number_input("Verse", min_verse, max_verse)

    # MultiVerse
    bible_df = df[(df['book'] == book_name) & (df['chapter'] == chapter)]
    all_verse = bible_df['verse'].unique().tolist()
    verse = st.sidebar.multiselect("Verse", all_verse, default=min_verse)
    selected_passage = bible_df[bible_df['verse'].isin(verse)]
    # st.dataframe(selected_passage)

    verse_list = selected_passage['verse'].astype(str).tolist()
    passage_details = "{} {}: {}".format(book_name,chapter, ", ".join(verse_list))
    st.write(passage_details)

    # Layout
    col1, col2 = st.columns(2)
    # joining all text 
    docx = ' '.join(selected_passage['text'].tolist())
    
    with col1:
        st.info("Details")
        for i, row in selected_passage.iterrows():
            st.write(f"[{row['verse']}] - {row['text']}")
            # st.write(row['text'])

    with col2:
        # st.success("Study Mode")
        # with st.expander("Visualize Entities"):
        #     # st.write(docx)
        #     render_entities(docx)

        with st.expander("Visualize Pos Tags"):
            tagged_docx = get_tags(docx)
            processed_tag = mytag_visualizer(tagged_docx)
            # st.write(processed_tag)
            stc.html(processed_tag, height=300, scrolling=True)

        with st.expander("Keywords"):
            processed_docx = nfx.remove_stopwords(docx)
            plot_most_common_tokens(processed_docx)

    with st.expander('Verse Curve'):
        plot_mendelhall_curve(docx)

    with st.expander('Word Frequency'):
        plot_word_freq_with_altair(docx)

    with st.expander("PoS Tags Plot"):
        plot_tags_value_count(docx)

    with st.expander("Word Cloud"):
        render_word_cloud(docx)


