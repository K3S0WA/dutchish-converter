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
    "spelling. It uses dictionary pronunciations, so words with context-dependent "
    "pronunciations may sometimes pick the wrong version."
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

if converted:
    st.button(
        "Copying is manual for now",
        disabled=True,
        help="Select the converted text above and copy it.",
    )

st.caption(
    "Built with CMUdict-style pronunciations. Unknown words appear in square brackets."
)
