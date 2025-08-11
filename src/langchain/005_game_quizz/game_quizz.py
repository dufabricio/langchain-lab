from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI


def _render_previous_questions(previous_questions: List[str]) -> str:
    if not previous_questions:
        return "(nenhuma)"
    return "\n".join(f"- {q}" for q in previous_questions)


def _normalize_answer(raw_answer: str) -> Optional[str]:
    cleaned = (raw_answer or "").strip().upper()
    if cleaned in {"A", "B", "C", "D"}:
        return cleaned
    # mapeia 1..4 -> A..D
    if cleaned in {"1", "2", "3", "4"}:
        return chr(ord("A") + int(cleaned) - 1)
    return None


def main() -> None:
    load_dotenv()

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    parser = JsonOutputParser()

    # Prompt para gerar UMA pergunta por vez, com 4 alternativas e gabarito.
    question_prompt = ChatPromptTemplate(
        [
            (
                "system",
                (
                    "Você é um gerador de perguntas de quiz. Gere UMA pergunta objetiva e "+
                    "clara sobre o tema '{tema}'. "
                    "Evite repetir qualquer pergunta do histórico a seguir.\n" 
                    "Histórico de perguntas já feitas:\n{historico}\n\n"
                    "Requisitos da pergunta:\n"
                    "- Múltipla escolha com 4 alternativas distintas (A, B, C, D).\n"
                    "- Deve haver somente uma alternativa correta.\n"
                    "- Linguagem simples, direta e sem ambiguidades.\n\n"
                    "{format_instructions}\n\n"
                    "Retorne no formato JSON conforme instruções. Campos esperados: "
                    "question (string), choices (lista com 4 itens; cada item com label A/B/C/D e text), "
                    "correct_label (A/B/C/D) e explanation (string)."
                ),
            ),
            (
                "human",
                (
                    "Gere uma pergunta agora sobre '{tema}'. "
                    "Nível: {nivel}."
                ),
            ),
        ],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    question_chain = question_prompt | model | parser

    asked_questions: List[str] = []
    score = 0
    total_questions = 5

    print("\n=== 🧠 Quiz interativo com LangChain ===")
    tema = input("Digite o tema/assunto do quiz: ").strip()
    if not tema:
        print("Tema vazio. Encerrando.")
        return

    try:
        nivel = input("Escolha a dificuldade (iniciante, intermediário, avançado): ").strip() or "iniciante"
    except KeyboardInterrupt:
        print("\nEncerrado.")
        return

    normalize_answer = RunnableLambda(_normalize_answer)

    def ask_and_score(question_payload: Dict[str, Any]) -> Tuple[int, str]:
        question_text = question_payload.get("question", "")
        choices = question_payload.get("choices", [])
        correct_label = question_payload.get("correct_label", "").upper()
        explanation = question_payload.get("explanation", "")

        print("\n" + "-" * 60)
        print(f"Pergunta: {question_text}")

        # Garantir ordenação A..D ao exibir
        def label_key(item: Dict[str, Any]) -> str:
            return str(item.get("label", "Z"))

        ordered_choices = sorted(choices, key=label_key)
        for idx, choice in enumerate(ordered_choices, start=1):
            label = str(choice.get("label", "?")).upper()
            text = str(choice.get("text", ""))
            print(f"  {idx}. ({label}) {text}")

        user_raw = input("Sua resposta (A, B, C, D ou 1-4): ")
        user_label = normalize_answer.invoke(user_raw)
        while user_label is None:
            user_raw = input("Entrada inválida. Responda com A, B, C, D ou 1-4: ")
            user_label = normalize_answer.invoke(user_raw)

        is_correct = user_label == correct_label
        if is_correct:
            print("✅ Correto!")
        else:
            print(f"❌ Incorreto. Gabarito: {correct_label}")
        if explanation:
            print(f"💡 Explicação: {explanation}")

        return (1 if is_correct else 0, question_text)

    for i in range(1, total_questions + 1):
        # Tentativas para tolerar respostas mal formatadas do modelo
        attempts = 0
        while attempts < 2:  # até 2 tentativas de gerar pergunta válida
            attempts += 1
            try:
                payload = {
                    "tema": tema,
                    "nivel": nivel,
                    "historico": _render_previous_questions(asked_questions),
                }
                question = question_chain.invoke(payload)
                gained, asked = ask_and_score(question)
                score += gained
                asked_questions.append(asked)
                break
            except Exception as e:  # noqa: BLE001
                if attempts >= 2:
                    print(f"\nNão foi possível gerar uma pergunta válida (erro: {e}). Pulando...")
                else:
                    print("\nRegenerando pergunta...")

        print(f"\nProgresso: {i}/{total_questions} | Pontuação: {score}")

    print("\n=== Resultado ===")
    print(f"Pontuação final: {score}/{total_questions}")
    if score >= 3:
        print("🏆 Parabéns! Você ganhou o game.")
    else:
        print("✨ Boa tentativa! Continue praticando para melhorar.")


if __name__ == "__main__":
    main()


