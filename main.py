import streamlit as st
from googletrans import Translator
import speech_recognition as sr

st.set_page_config(page_title="Guide", layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def translate_to_amharic(text):
    translator = Translator()
    with st.spinner('Translating...'):
        translation = translator.translate(text, dest='am')
    return translation.text

def translate_to_english(text):
    translator = Translator()
    with st.spinner('Translating...'):
        translation = translator.translate(text, src='am', dest='en')
    return translation.text

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')
        return text
    except sr.UnknownValueError:
        st.error("Could not understand audio")
    except sr.RequestError as e:
        st.error(f"Service error; {e}")

def display_translated_text(translation, title="Translated Text"):
    st.success(f"{title}: {translation}")

def main():
    st.header("Multilingual Translation Application")

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("English to Amharic")
            input_text = st.text_area("Enter English text:", height=150)
            if st.button("Translate to Amharic", key='en2am'):
                if input_text:
                    translated_text = translate_to_amharic(input_text)
                    display_translated_text(translated_text, "Translated to Amharic")
                else:
                    st.error("Please enter some text to translate.")

        with col2:
            st.subheader("Speech Translation (English to Amharic)")
            if st.button("Start Listening", key='speech2am'):
                recognized_text = recognize_speech()
                if recognized_text:
                    display_translated_text(recognized_text, "Recognized English Text")
                    translated_text = translate_to_amharic(recognized_text)
                    display_translated_text(translated_text, "Translated to Amharic")

        with col3:
            st.subheader("ከአማርኛ ወደ እንግሊዘኛ")
            input_amharic_text = st.text_area("የአማርኛ ጽሑፍ አስገባ:", height=150)
            if st.button("ወደ እንግሊዝኛ ተርጉም", key='am2en'):
                if input_amharic_text:
                    translated_text = translate_to_english(input_amharic_text)
                    display_translated_text(translated_text, "Translated to English")
                else:
                    st.error("Please enter some text to translate.")

    st.markdown("---")
    st.caption("© 2024 Guzo. All rights reserved.")
if __name__ == "__main__":
    main()
