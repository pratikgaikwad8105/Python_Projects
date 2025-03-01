import streamlit as st

if "selected_voice" not in st.session_state:
    st.session_state.selected_voice = "Rachel"

voices = {
    "Rachel": {"id": "21m00Tcm4TlvDq8ikWAM",
               "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/comm2022-portraits/el/Sarah.jpg"},
    "Domi": {"id": "AZnzlk1XvdvUeBnXmlld",
             "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/comm2022-portraits/el/Aria.jpg"},
    "Bella": {"id": "EXAVITQu4vr4xnSDxMaL",
              "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/comm2022-portraits/el/River.jpg"},
    "Antoni": {"id": "ErXwobaYiN019PkySvjV",
               "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/comm2022-portraits/el/Roger.jpg"},
    "Elli": {"id": "MF3mGyEYCl7XYWbV9V6O",
             "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/comm2022-portraits/el/Catherine.jpg"},
    "Josh": {"id": "TxGEqnHWrfWFTfGW9XjX",
             "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/comm2022-portraits/el/Chris.jpg"},
    "Charlie": {"id": "IKne3meq5aSn9XLyUdCD",
                "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/pw-portraits/multi-lingual/Echo.jpg"},
    "Sam": {"id": "yoZ06aMxZJJ28mfd3POQ",
            "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/pw-portraits/multi-lingual/Onyx.jpg"},
    "Mimi": {"id": "zrHiDhphv9ZnVXBqCLjz",
             "avatar": "https://wwwnaturalreaderscom.s3.amazonaws.com/pw-portraits/multi-lingual/Nova.jpg"},
}


def ui():
    st.title("🔊 Text-To-Speech (Multilingual)")

    text = st.text_area("Enter text:", value="Type something...", key="text_input")

    st.write("### 🎤 Select a Voice")

    cols = st.columns(3)

    for i, (name, data) in enumerate(voices.items()):
        with cols[i % 3]:
            st.markdown(f"""
                <div style="
                    display: flex; 
                    justify-content: center; 
                    padding-right: 10px; 
                    margin-bottom: 10px;">
                    <img src="{data['avatar']}" width="130" 
                        style="border-radius: 50%; object-fit: cover;">
                </div>
            """, unsafe_allow_html=True)

            if st.button(name, key=f"voice_{name}", use_container_width=True):
                st.session_state.selected_voice = name

    st.success(f"🎤 Selected Voice: **{st.session_state.selected_voice}**")

    return text, voices[st.session_state.selected_voice]["id"]
