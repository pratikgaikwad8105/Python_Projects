import streamlit as st
import app


st.title("Healthcare Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask Me Anything!")

with st.chat_message("assistant"):
    st.markdown("How can I assist you with a health-related topic today?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = app.chat(prompt).choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})


