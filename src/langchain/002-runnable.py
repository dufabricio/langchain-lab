""" Realizando as importações """

from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableSequence
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Simple runnable

def add_one(x: int) -> int:
    return x + 1

add_one_runnable = RunnableLambda(add_one)

print(add_one_runnable.invoke(1));

# Parametrizing a runnable

def mutiply_by_two(value: int) -> int:
    return value * 2

multiply_runnable = RunnableLambda(mutiply_by_two)

print(multiply_runnable.invoke(2))

# Using a runnable in a chain

seq = RunnableSequence(
    RunnableLambda(mutiply_by_two),
    RunnableLambda(add_one)
)

print(seq.invoke(2))

