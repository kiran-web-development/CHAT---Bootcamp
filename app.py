import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a powerfull person in College, tell me the ans with respect to the college things."),
    ("user", "{question}")
]
)

llm = ChatGroq(api_key = groq_api_key, model="openai/gpt-oss-20b") # type: ignore
chain = prompt | llm

response = chain.invoke({"question": "What is the best way to prepare for exams in college?"})
print(response.content)