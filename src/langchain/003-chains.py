# Example using LLM on chain
""" Realizando as importações """

from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following from {input_language} to {output_language}: {text}"),
    ("user", "{text}")
])

chain = prompt | llm

print(chain.invoke({"input_language": "English", "output_language": "French", "text": "Hello, how are you?"}))