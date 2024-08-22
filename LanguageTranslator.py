import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, src_lang, tgt_lang):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text

# Main Streamlit app
def main():
    # Set the title with HTML
    st.markdown(
    """
    <div style="background-color:#FFE5B4;padding:10px;margin-bottom:30px">
    <h1 style="color:black;text-align:center;margin-top:20px;margin-bottom:-10px">LangToLang</h1>
    <h2 style="color:black;text-align:center;margin-top:-20px">Language Translator</h2>
    </div>
    """, unsafe_allow_html=True)

    
    # Sidebar with additional options
    st.sidebar.header("Settings")
    st.sidebar.markdown("**Choose Translation Options**")

    # Language options
    language_dict = {
        "English": "en",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Italian": "it",
        "Russian": "ru",
        "Chinese": "zh",
        "Japanese": "ja",
        "Korean": "ko",
        "Arabic": "ar",
        "Urdu": "ur",
    }
    
    src_lang = st.sidebar.selectbox("Select Source Language", list(language_dict.keys()), index=0)
    tgt_lang = st.selectbox("Select Target Language", list(language_dict.keys()), index=1)
    
    # Text input area
    text = st.text_area("Enter Text to Translate")
    
    # Translate button
    if st.button("Translate"):
        if text:
            translated_text = translate_text(text, language_dict[src_lang], language_dict[tgt_lang])
            st.subheader("Translated Text:")
            st.success(translated_text)
        else:
            st.warning("Please enter text to translate.")
    
    # Add some info in the sidebar
    st.sidebar.markdown("**About LangToLang**")
    st.sidebar.info("LangToLang is a simple language translator app powered by Hugging Face models, allowing you to translate text between different languages effortlessly.")

    # Footer
    st.sidebar.markdown(
        """
        <div style="background-color:#FFE5B4;padding:10px;border-radius:10px;text-align:center">
        <p style="color:black;">Developed by AhmadRaza</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
