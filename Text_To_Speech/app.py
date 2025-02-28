import streamlit as st
from tts_api import generate_speech
from ui import ui


if "selected_voice" not in st.session_state:
    st.session_state.selected_voice = "Rachel"

st.set_page_config(page_title="Text-TO-Speech(TTS)V1.0", page_icon="🔊")


text, voice_id = ui()


if st.button("🚀 Generate Speech"):
    if text.strip():
        with st.spinner("🎙️ Generating speech..."):
            try:
                audio_bytes = generate_speech(text, voice_id)  # Get audio

                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(label="⬇️ Download Audio",
                                   data=audio_bytes,
                                   file_name="speech.mp3",
                                   mime="audio/mp3")

            except Exception as e:
                st.error(f"❌ {e}")
    else:
        st.error("⚠️ Please enter some text.")
