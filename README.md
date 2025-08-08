# 💬 Chat Console com LangChain usando PDM

Este é um exemplo simples de como usar LangChain para criar um chat interativo via console que aceita input do usuário.

## 🚀 Como Executar

### 1. Instale as dependências com PDM

```bash
pdm install
```

### 2. Configure sua API Key

1. Copie o arquivo de exemplo:
```bash
cp env.example .env
```

2. Edite o arquivo `.env` e substitua os valores de exemplo pelas suas chaves reais:
```env
OPENAI_API_KEY=sua_chave_openai_real_aqui

# Outras APIs (opcionais)
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui
GOOGLE_API_KEY=sua_chave_google_aqui

# LangSmith (opcional - apenas se quiser rastreamento)
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_API_KEY=sua_chave_langchain_aqui
# LANGCHAIN_PROJECT=langchain-lab
```

**⚠️ Importante:** Apenas a `OPENAI_API_KEY` é obrigatória para este exemplo.

### 3. Execute o exemplo

```bash
pdm run python simple_chat_console.py
```

## 🎯 O que este exemplo faz

- ✅ Carrega a API key do arquivo `.env`
- ✅ Inicializa um modelo ChatOpenAI (gpt-3.5-turbo)
- ✅ Cria um loop interativo para capturar input do usuário
- ✅ Envia perguntas para o modelo e exibe as respostas
- ✅ Permite sair digitando 'sair', 'exit', 'quit' ou 'bye'
- ✅ Inclui tratamento completo de erros
- ✅ Interface amigável com emojis
- ✅ Usa apenas PDM (não depende de pip)
- ✅ Desabilita automaticamente o LangSmith se não configurado

## 💡 Exemplo de Uso

```