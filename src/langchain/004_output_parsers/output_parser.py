from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
import json

# Carregamento das variáveis de ambiente presentes em .env
load_dotenv()


model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

# Criando o analisador de saída
parser = JsonOutputParser()

prompt_template = ChatPromptTemplate([
    ("system", "Você é um assistente especialista em {especialidade} e responde specificacoes tecnicas para {item} \
        .\n {format_instructions}\n Pergunta do usuário: {input}"),
],partial_variables={"format_instructions": parser.get_format_instructions()})


chain = prompt_template | model | parser

input = input("Você: ")


output = chain.invoke({"input": input,"especialidade": "fotografia", "item": "lentes objetivas"})

print(json.dumps(output, indent=4))