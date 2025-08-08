#!/usr/bin/env python3
"""
Chat console simples usando LangChain.

Este módulo implementa um chat básico que aceita input do usuário via console
e responde usando OpenAI através do LangChain.

Uso:
    pdm run python -m src.langchain.simple_chat
    ou
    pdm run python src/langchain/simple_chat/main.py
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


def setup_environment():
    """Configura o ambiente e carrega variáveis."""
    load_dotenv()
    
    # Desabilita LangSmith se não configurado para evitar erros
    if not os.getenv("LANGCHAIN_API_KEY"):
        os.environ["LANGCHAIN_TRACING_V2"] = "false"


def validate_api_key():
    """Valida se a API key do OpenAI está configurada."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("❌ Erro: OPENAI_API_KEY não encontrada ou não configurada!")
        print("📝 Configure sua API key no arquivo .env")
        print("💡 Passos:")
        print("   1. cp env.example .env")
        print("   2. Edite o arquivo .env e substitua 'your_openai_api_key_here' pela sua chave real")
        return None
    return api_key


def create_llm(api_key: str):
    """Cria e configura o modelo LLM."""
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=api_key
    )


def create_system_message():
    """Cria a mensagem de sistema que define o comportamento do assistente."""
    return SystemMessage(
        content="Você é um assistente útil e amigável. "
               "Responda de forma clara e concisa às perguntas do usuário em português."
    )


def chat_loop(llm, system_message):
    """Loop principal do chat interativo."""
    print("🤖 Chat com LangChain - OpenAI")
    print("💬 Digite suas perguntas ou 'sair' para encerrar")
    print("🔧 Executado com PDM - Módulo src.langchain.simple_chat")
    print("-" * 60)
    
    while True:
        # Captura input do usuário
        user_input = input("\n👤 Você: ").strip()
        
        # Verifica se o usuário quer sair
        if user_input.lower() in ['sair', 'exit', 'quit', 'bye']:
            print("👋 Até logo!")
            break
        
        # Verifica se o input não está vazio
        if not user_input:
            print("⚠️ Por favor, digite alguma coisa!")
            continue
        
        try:
            # Cria a mensagem do usuário
            human_message = HumanMessage(content=user_input)
            
            # Envia as mensagens para o modelo
            messages = [system_message, human_message]
            
            print("🤖 Assistente: ", end="", flush=True)
            
            # Chama o modelo e obtém a resposta
            response = llm.invoke(messages)
            
            # Exibe a resposta
            print(response.content)
            
        except Exception as e:
            print(f"❌ Erro ao processar sua pergunta: {str(e)}")
            print("💡 Tente novamente ou verifique sua conexão com a internet")


def main():
    """Função principal que executa o chat interativo."""
    try:
        # Configura ambiente
        setup_environment()
        
        # Valida API key
        api_key = validate_api_key()
        if not api_key:
            return
        
        # Cria o modelo LLM
        llm = create_llm(api_key)
        
        # Cria mensagem de sistema
        system_message = create_system_message()
        
        # Inicia o chat
        chat_loop(llm, system_message)
        
    except Exception as e:
        print(f"❌ Erro ao inicializar o chat: {str(e)}")
        print("💡 Verifique sua API key e conexão com a internet")


if __name__ == "__main__":
    main()
