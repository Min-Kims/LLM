# deactivate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv; load_dotenv()

llm = ChatOpenAI()
print(llm.invoke("Cost of $355.39 + $924.87 + $721.2 + $1940.29 + $573.63 + $65.72 + $35.00 + $552.00 + $76.16 + $29.12"))
# 답: 5273.38 US$
