# 🧪 LangChain Lab

Um projeto Python básico para experimentar e aprender **LangChain** e **LangGraph** usando PDM como gerenciador de dependências.

## 📋 Pré-requisitos

- Python 3.9+
- PDM instalado (`pip install pdm`)
- Chaves de API (OpenAI, Anthropic, etc.)

## 🚀 Configuração Inicial

### 1. Clone e configure o projeto

```bash
# Clone ou baixe o projeto
cd langchain-lab

# Instale as dependências
pdm install

# Configure as variáveis de ambiente
cp env.example .env
# Edite o arquivo .env com suas chaves de API
```

### 2. Configure suas API Keys

Edite o arquivo `.env` e adicione suas chaves:

```env
OPENAI_API_KEY=sua_chave_openai_aqui
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui
LANGCHAIN_API_KEY=sua_chave_langchain_aqui
```

## 📁 Estrutura do Projeto

```
langchain-lab/
├── src/
│   ├── langchain_examples/      # Exemplos de LangChain
│   │   ├── basic_chat.py        # Chat básico com OpenAI
│   │   ├── prompt_template.py   # Templates de prompt
│   │   └── web_scraping.py      # Web scraping e análise
│   └── langgraph_examples/      # Exemplos de LangGraph
│       ├── simple_agent.py      # Agente conversacional
│       ├── workflow_example.py  # Workflow de análise
│       └── state_machine.py     # Máquina de estados
├── tests/                       # Testes (a implementar)
├── docs/                        # Documentação adicional
├── pyproject.toml              # Configuração PDM
├── env.example                 # Exemplo de variáveis de ambiente
└── README.md                   # Este arquivo
```

## 🎯 Exemplos Disponíveis

### LangChain Examples

#### 1. Chat Básico (`basic_chat.py`)
```bash
pdm run python src/langchain_examples/basic_chat.py
```
- Chat simples com OpenAI
- Configuração básica de LLM
- Tratamento de erros

#### 2. Prompt Templates (`prompt_template.py`)
```bash
pdm run python src/langchain_examples/prompt_template.py
```
- Uso de ChatPromptTemplate
- Chains com StrOutputParser
- Templates com variáveis

#### 3. Web Scraping (`web_scraping.py`)
```bash
pdm run python src/langchain_examples/web_scraping.py
```
- WebBaseLoader para scraping
- Divisão de texto em chunks
- Análise de conteúdo web

### LangGraph Examples

#### 1. Agente Simples (`simple_agent.py`)
```bash
pdm run python src/langgraph_examples/simple_agent.py
```
- Agente conversacional interativo
- StateGraph básico
- Controle de fluxo condicional

#### 2. Workflow de Análise (`workflow_example.py`)
```bash
pdm run python src/langgraph_examples/workflow_example.py
```
- Pipeline de análise de texto
- Múltiplas etapas sequenciais
- Geração de relatório final

#### 3. Máquina de Estados (`state_machine.py`)
```bash
pdm run python src/langgraph_examples/state_machine.py
```
- Sistema de processamento de pedidos
- Estados complexos com validações
- Roteamento condicional avançado

## 🛠️ Comandos PDM Úteis

```bash
# Instalar dependências
pdm install

# Adicionar nova dependência
pdm add nome-do-pacote

# Adicionar dependência de desenvolvimento
pdm add -dG dev nome-do-pacote

# Executar scripts
pdm run python script.py

# Atualizar dependências
pdm update

# Remover dependência
pdm remove nome-do-pacote

# Mostrar dependências instaladas
pdm list

# Ativar shell virtual
pdm shell
```

## 🧪 Desenvolvimento

### Executando Testes
```bash
pdm run pytest
```

### Formatação de Código
```bash
# Black
pdm run black src/

# isort
pdm run isort src/

# Flake8
pdm run flake8 src/
```

### Adicionando Novos Exemplos

1. Crie um novo arquivo na pasta apropriada (`langchain_examples/` ou `langgraph_examples/`)
2. Siga o padrão dos exemplos existentes
3. Inclua tratamento de erros e documentação
4. Adicione instruções de execução neste README

## 📚 Recursos Úteis

- [Documentação LangChain](https://python.langchain.com/)
- [Documentação LangGraph](https://langchain-ai.github.io/langgraph/)
- [PDM Documentation](https://pdm.fming.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🔧 Troubleshooting

### Problemas Comuns

1. **Erro de API Key**
   - Verifique se o arquivo `.env` existe e está configurado
   - Confirme se as chaves estão válidas e ativas

2. **Erro de Instalação de Dependências**
   - Verifique se o PDM está atualizado: `pip install --upgrade pdm`
   - Tente limpar o cache: `pdm cache clear`

3. **Erro de Importação**
   - Certifique-se de estar executando com `pdm run`
   - Verifique se todas as dependências foram instaladas

4. **Erro de Conexão Web**
   - Verifique sua conexão com a internet
   - Alguns exemplos de web scraping podem falhar com URLs indisponíveis

### Logs e Debug

Para debugar problemas, você pode:

```bash
# Executar com logs detalhados
export LANGCHAIN_VERBOSE=true
pdm run python seu_script.py

# Verificar versões instaladas
pdm list
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se você encontrar problemas ou tiver dúvidas:

1. Verifique a seção de [Troubleshooting](#-troubleshooting)
2. Consulte a documentação oficial do [LangChain](https://python.langchain.com/) e [LangGraph](https://langchain-ai.github.io/langgraph/)
3. Abra uma issue no repositório do projeto

---

**Happy Coding! 🚀**
