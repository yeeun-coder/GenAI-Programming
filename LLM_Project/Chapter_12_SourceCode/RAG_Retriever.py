from dotenv import load_dotenv
from openai import OpenAI
import os
# langchain.chains.combine_documents-> langchain_classic.chains.combine_documents
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser   # String output parser

load_dotenv()

# Input api_key in the sidebar
strOpenAI_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file
   
# Call OpenAI() method
client = OpenAI(api_key = strOpenAI_API_Key)

# RAG Retriever with Chroma and OpenAI Embeddings
from langchain_openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings(model='text-embedding-3-large')

# Load LLM(OpenAI)  
from langchain_openai import ChatOpenAI
LLM = ChatOpenAI(model="gpt-4o")

# Load Chroma store
from langchain_chroma import Chroma
print("Loading existing Chroma DB")
persist_directory = '../chroma_DB'

vector_DB = Chroma(
    persist_directory=persist_directory, 
    embedding_function=embedding
)

# Create retriever
retriever = vector_DB.as_retriever(k=3)   # Set k to retrieve top 3 documents

# Create Question answering prompt
question_answering_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "사용자의 질문에 대해 아래 context에 기반하여 답변하라.:\n\n{context}",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

document_chain = create_stuff_documents_chain(LLM, question_answering_prompt) | StrOutputParser()

# Create Query augmentation prompt
query_augmentation_prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="messages"), # Include chat history
        (
            "system",
            "기존의 대화 내용에 기반하여 사용자의 아래 질문의 의도를 파악하여 명료한 한 문장의 질문으로 변환하라. 대명사나 이, 저, 그와 같은 표현을 명확한 명사로 표현하라. :\n\n{query}",
        ),
    ]
)

# Create Query augmentation chain
query_augmentation_chain = query_augmentation_prompt | LLM | StrOutputParser()
