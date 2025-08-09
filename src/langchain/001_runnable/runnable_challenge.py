from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableSequence
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()



print(" CHALLENGE: Chain of Runnables reverse word")

# create runnable chain nodes

# NODE 1
runnable_1_start = RunnablePassthrough()

# NODE 1.1
def reverse_word(word: str) -> str:
    return word[::-1] 
runnable_2_reverse = RunnableLambda(reverse_word)


# NODE 1.2
def count_chars(word: str) -> str:
    return len(word) 
runnable_3_len = RunnableLambda(count_chars)


# NODE 3 - Final node
runnable_4_reverse_and_count_chars = RunnableParallel(
    {
        "total_chars": runnable_3_len,
        "reverse_word": runnable_2_reverse
    })

runnable_5_finish_status = RunnablePassthrough.assign(status=lambda json:"finished" ) 
# create runnable chain
chain = runnable_1_start | runnable_4_reverse_and_count_chars | runnable_5_finish_status


def start_chat() -> str:
    return input("Enter a phrase or word: ")


print(chain.invoke(start_chat()))