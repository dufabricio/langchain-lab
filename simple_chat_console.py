#!/usr/bin/env python3
"""
Exemplo simples de LangChain com input do usuário via console.
Este script cria um chat básico usando OpenAI que responde às perguntas do usuário.

Para executar:
    pdm run python simple_chat_console.py
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def main():
    """Função principal que executa o chat interativo."""
    
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Verifica se a API key do OpenAI está configurada
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("❌ Erro: OPENAI_API_KEY não encontrada ou não configurada!")
        print("📝 Configure sua API key no arquivo .env")
        print("💡 Passos:")
        print("   1. cp env.example .env")
        print("   2. Edite o arquivo .env e substitua 'your_openai_api_key_here' pela sua chave real")
        return
    
    try:
        # Inicializa o modelo LLM (OpenAI)
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=api_key
        )
        
        print("🤖 Chat com LangChain - OpenAI")
        print("💬 Digite suas perguntas ou 'sair' para encerrar")
        print("🔧 Executado com PDM")
        print("-" * 50)
        
        # Mensagem de sistema para definir o comportamento do assistente
        system_message = SystemMessage(
            content="Você é um assistente útil e amigável. "
                   "Responda de forma clara e concisa às perguntas do usuário em português."
        )
        
        # Loop principal do chat
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
    
    except Exception as e:
        print(f"❌ Erro ao inicializar o modelo: {str(e)}")
        print("💡 Verifique sua API key e conexão com a internet")

if __name__ == "__main__":
    main()
