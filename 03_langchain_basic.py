from langchain_openai import ChatOpenAI; from dotenv import load_dotenv; load_dotenv()

print(ChatOpenAI().invoke("Hello. Do you know Psy?"))

