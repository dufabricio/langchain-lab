from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# setup
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)


# assistent conversation loop
conversation = [
    SystemMessage(content="Você é um assistente especialista em fotografia e responde questões tecnicas e conceituais sobre as perguntas"),
]

while True:
    # Captura input do usuário
    chat_input = input("\n👤 you: ").strip()
    
    # Verifica se quer sair
    if chat_input.lower() in ['sair', 'exit', 'quit']:
        print("👋 Cya!")
        break
        
    conversation.append(HumanMessage(content=chat_input))
    response = model.invoke(conversation)
    conversation.append(AIMessage(content=response.content))
    print(f"🤖 agent: {response.content}")
    
print(conversation)    






