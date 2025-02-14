from groq import Groq
import streamlit as st
import re

client = Groq(
    api_key="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",
)


def chat(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        model="deepseek-r1-distill-llama-70b",
    )

    return chat_completion


def healthcare_chatbot(user_input):
    response = chat(user_input)
    return response.choices[0].message.content





def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can you assist you today?")
    if st.button("Submit"):
        healthcare_chatbot("skip the thinking text. No preamble")
        if user_input:
            st.write("User : ", user_input)
            with st.spinner("Processing your Question"):
                response = healthcare_chatbot(user_input)
            st.write("Bot", re.sub("""Bot <think></think>""", "", response))
        else:
            st.write("Please Enter text")

main()
