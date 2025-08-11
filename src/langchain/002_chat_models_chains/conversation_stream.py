from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import asyncio

# setup
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)


async def start_chat():
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
        
        print(f"🤖 agent: ")
        
        all_chunks = []
        async for chunk in model.astream(conversation):
            all_chunks.append(chunk.content)
            print(chunk.content, end="", flush=True)
        
        response = "".join(all_chunks)
        
        conversation.append(AIMessage(content=response))
        
    print(conversation)    


asyncio.run(start_chat())



