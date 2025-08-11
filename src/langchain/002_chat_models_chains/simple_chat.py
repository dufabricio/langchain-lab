#!/usr/bin/env python3
"""
Chat console simples usando LangChain.

Exemplo didático e simplificado de um chat básico com OpenAI.

Uso:
    pdm run python -m src.langchain.simple_chat
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


def setup_chat():
    """Configura o ambiente e cria o modelo de chat."""
    # Carrega variáveis do arquivo .env
    load_dotenv()
    
    # Desabilita LangSmith se não configurado
    if not os.getenv("LANGCHAIN_API_KEY"):
        os.environ["LANGCHAIN_TRACING_V2"] = "false"
    
    # Verifica se a API key está configurada
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("❌ Erro: OPENAI_API_KEY não encontrada!")
        print("💡 Configure sua API key no arquivo .env")
        return None
    
    # Cria o modelo de chat
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=api_key
    )
    
    return llm


def main():
    """Função principal do chat."""
    # Configura o chat
    llm = setup_chat()
    if not llm:
        return
    
    # Mensagem de sistema que define o comportamento do assistente
    system_message = SystemMessage(
        content="Você é um assistente útil e amigável. Responda em português."
    )
    
    # Interface do chat
    print("🤖 Chat com LangChain - OpenAI")
    print("💬 Digite suas perguntas ou 'sair' para encerrar")
    print("-" * 50)
    
    # Loop principal do chat
    while True:
        # Captura input do usuário
        user_input = input("\n👤 Você: ").strip()
        
        # Verifica se quer sair
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("👋 Até logo!")
            break
        
        # Verifica se digitou algo
        if not user_input:
            print("⚠️ Digite alguma pergunta!")
            continue
        
        try:
            # Prepara as mensagens
            messages = [
                system_message,
                HumanMessage(content=user_input)
            ]
            
            # Obtém resposta do modelo
            print("🤖 Assistente: ", end="", flush=True)
            response = llm.invoke(messages)
            print(response.content)
            
        except Exception as e:
            print(f"❌ Erro: {str(e)}")


if __name__ == "__main__":
    main()
