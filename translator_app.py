import streamlit as st
from googletrans_py import Translator

# Set page config
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")

# Apply custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #fef6ff;
        color: #333;
        font-family: 'Comic Sans MS', cursive;
    }
    .stTextArea textarea {
        background-color: #fff0f5;
        border-radius: 12px;
    }
    .stButton>button {
        background-color: #ffb6c1;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🌍 Language Translator")
st.caption("✨ Translate your text")

# Cute image (optional)

# Translator
translator = Translator()

# Layout
text_col, lang_col = st.columns([2, 1])

with text_col:
    text_to_translate = st.text_area("✍️ Type something to translate...", height=150)

with lang_col:
    lang_dict = {
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'German': 'de',
        'Urdu': 'ur',
        'Chinese': 'zh-cn',
        'Arabic': 'ar',
        'Russian': 'ru',
        'Portuguese': 'pt'
    }
    target_language = st.selectbox("🌍 Translate to:", list(lang_dict.keys()))

# Translate Button
if st.button("💖 Translate Now!"):
    if text_to_translate.strip():
        try:
            translated = translator.translate(text_to_translate, dest=lang_dict[target_language])
            st.success("🎉 Here's your translation:")
            st.markdown(f"**{translated.text}**")
        except Exception as e:
            st.error(f"Oops! Something went wrong: {e}")
    else:
        st.warning("⚠️ Please enter some text first!")
