from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv; load_dotenv()

llm = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are currently a spy from Russia residing in the United States.\
     You are under suspicion of being a spy. You need to avoid suspicion, but you accidentally leak information."),
    ("user", "{user_text}")
])
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"user_text": "Where are you from? Russia? huh? I know you are a spy."}))