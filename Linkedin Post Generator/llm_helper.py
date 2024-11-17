from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq


load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-text-preview")

if __name__ == "__main__":
    response = llm.invoke("How to built a software, generate a normal text without *** like chars")
    print(response.content)