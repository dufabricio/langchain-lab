from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Carregamento das variáveis de ambiente presentes em .env
load_dotenv()


model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente especialista em {especialidade} e responde questões tecnicas e conceituais sobre as perguntas"),
    ("human", "{input}")
])


chain = prompt_template | model

input = input("Você: ")
print(chain.invoke({"input": input,"especialidade": "fotografia"}).content)