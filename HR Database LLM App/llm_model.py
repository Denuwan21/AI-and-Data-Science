from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt 
from langchain.prompts import FewShotPromptTemplate
from langchain_community.agent_toolkits import create_sql_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.agent_types import AgentType

from few_short_queries import few_shorts

MODEL_API_KEY = "##################"

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash-exp",
    google_api_key = MODEL_API_KEY
)

def model_function():
    db_user = 'root'
    db_pass = ''
    db_host = 'localhost'
    db_name = 'human_resouce'

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}", sample_rows_in_table_info = 3)
    print(db.table_info)

    emb = OllamaEmbeddings(model="nomic-embed-text")

    to_victorize = ["".join(str(i) for i in sample.values()) for sample in few_shorts]

    vector_db = Chroma.from_texts(to_victorize, embedding=emb, metadatas=few_shorts)

    sample_selector = SemanticSimilarityExampleSelector(
        vectorstore=vector_db,
        k=2,
    )

    prompt_templete = PromptTemplate(
        input_variables=['Question', 'SQLQuery', 'SQLResult', 'Answer'],
        template="\nQuestion : {Question}\nSQLQuery : {SQLQuery}\nSQLResult : {SQLResult}\nAnswer"
    )

    few_short_prompt = FewShotPromptTemplate(
        example_selector=sample_selector,
        example_prompt=prompt_templete,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=['input', 'table_info', 'top_k', 'agent_scratchpad'],
    )

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", few_short_prompt.format(input="User's input goes here", table_info="Table info here", top_k="5")),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    new_db_chain = create_sql_agent(
        llm=llm, 
        db=db,
        verbose = True,
        agent_type="openai-tools",
        use_query_checker=True,
        prompt=chat_prompt
    )

    return new_db_chain

if __name__=="__main__":
    new_db_chain = model_function()