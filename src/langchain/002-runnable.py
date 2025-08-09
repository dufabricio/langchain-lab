from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableSequence
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()



print("EXAMPLE:Simple runnable")

def add_one(x: int) -> int:
    return x + 1

add_one_runnable = RunnableLambda(add_one)

print(add_one_runnable.invoke(1));




print("EXAMPLE: Parametrizing a runnable")

def mutiply_by_two(value: int) -> int:
    return value * 2

multiply_runnable = RunnableLambda(mutiply_by_two)

print(multiply_runnable.invoke(2))



print("EXAMPLE: Using a runnable in a chain")

seq = RunnableSequence(
    RunnableLambda(mutiply_by_two),
    RunnableLambda(add_one)
)

print(seq.invoke(2))




print("EXAMPLE: runnable passthrough with assign")

sequence = add_one_runnable | { "multiply_task1":multiply_runnable, "multiply_task2":multiply_runnable } 
print(sequence.invoke(3))




print(" EXAMPLE: runnable passthrough with assign")

sequence  = RunnablePassthrough( {"num":5} ) | RunnableLambda.assign(lambda x: x["num"] * 5) | RunnablePassthrough() 
print(sequence.invoke())





