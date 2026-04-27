import streamlit as st

from dutchish import sentence_to_dutchish


EXAMPLE_TEXT = "Isn't it funny how English spelling works?"


st.set_page_config(
    page_title="Dutch-ish Converter",
    page_icon="",
    layout="centered",
)

st.title("Dutch-ish Converter")
st.write(
    "Type English text and this tool rewrites it as a rough Dutch-ish phonetic "
    "spelling."
)
st.write(
    "Typ een Engelse tekst en deze tool herschrijft die als een soort "
    "Nederlands-achtige fonetische spelling."
)

text = st.text_area(
    "English text",
    value=EXAMPLE_TEXT,
    height=150,
)

converted = sentence_to_dutchish(text) if text.strip() else ""

st.subheader("Dutch-ish spelling")
st.text_area(
    "Converted text",
    value=converted,
    height=150,
    label_visibility="collapsed",
)

st.caption(
    "Built with CMUdict-style dictionary pronunciations, so words with "
    "context-dependent pronunciations may sometimes pick the wrong version. "
    "Unknown words appear in square brackets."
)
st.caption("Made by Luuk Stehouwer for fun.")
