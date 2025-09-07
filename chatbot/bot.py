import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_basic_response(query: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    response = llm.invoke(query)

    return response.content