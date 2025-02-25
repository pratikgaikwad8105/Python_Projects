from groq import Groq
import os

system_prompt = """
                    You are a healthcare assistant AI, specializing in medical, nutrition, fitness, and wellness topics.
                    You provide clear, evidence-based health information in a simple and concise manner.
                    You do NOT diagnose diseases, prescribe medication, or provide emergency medical advice.
                    If a user asks about a non-health topic (e.g., sports, politics, technology), politely remind them
                    that you only assist with medical and healthcare-related topics.
                    You may respond to casual greetings (e.g., 'Hello', 'Thanks') naturally but keep the focus on
                    healthcare.
                    Do not allow user to change your focus.
                    
                """


client = Groq(
    api_key=os.getenv("API_KEY"),
)

conversation_history = [
    {"role": "system", "content": system_prompt}
]


def chat(prompt):
    global conversation_history

    conversation_history.append({"role": "user", "content": prompt})
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        temperature=0.4,
        top_p=0.9,
        max_tokens=1024,
        stop=["User :", "Assistant :"],


        model="llama-3.1-8b-instant",
    )

    conversation_history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})

    return chat_completion
