# 3.11.6
from langchain.agents import create_sql_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv; load_dotenv()

llm = ChatOpenAI(
    temperature=0.1,
    model_name="gpt-4-1106-preview",
)
db = SQLDatabase.from_uri("sqlite:///movies.sqlite")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
)

agent.invoke(
    "Give me the movies that have the highest votes but the lowest budgets and give me the name of their directors also include their gross revenue."
)