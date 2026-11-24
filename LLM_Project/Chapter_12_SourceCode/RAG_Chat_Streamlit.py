import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
import RAG_Retriever

LLM = ChatOpenAI(model="gpt-4o-mini")   # Initialize LangChain Chatbot model

# User query processing and getting AI response
def get_ai_response(messages, docs):    
    response = RAG_Retriever.document_chain.stream({
        "messages": messages,
        "context": docs
    })

    for chunk in response:
        yield chunk

# Streamlit App
st.title("💬 GPT-4o Langchain Chat")    # Streamlit App Title
st.caption("🚀 A Streamlit Chatbot powered by OpenAI")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage("너는 문서에 기반해 답변하는 도시 정책 전문가야 "),  
        AIMessage("How can I help you?")
    ]

# Display messages on Streamlit screen  
for msg in st.session_state.messages:
    if msg.content:
        if isinstance(msg, SystemMessage):
            st.chat_message("system").write(msg.content)
        elif isinstance(msg, AIMessage):
            st.chat_message("assistant").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)

# Handle user input
if prompt := st.chat_input():
    st.chat_message("user").write(prompt)                   # Display user message
    st.session_state.messages.append(HumanMessage(prompt))  # Store user message

    print("User\t:", prompt)

    augmented_query = RAG_Retriever.query_augmentation_chain.invoke({
        "messages": st.session_state["messages"],
        "query": prompt,
    })
    print("augmented_query\t", augmented_query)

    # Retrieve relevant documents
    print("관련 문서 검색...")
    docs = RAG_Retriever.retriever.invoke(f"{prompt}\n{augmented_query}")

    for doc in docs:
        print('---------------')
        print(doc)   
        with st.expander(f"**문서:** {doc.metadata.get('source', '알 수 없음')}"):
            # Display document metadata and content(Page info, content)
            st.write(f"**page:**{doc.metadata.get('page', '')}")
            st.write(doc.page_content)
    print("===============")
        
    with st.spinner(f"AI가 답변을 준비 중입니다... '{augmented_query}'"):
        response = get_ai_response(st.session_state["messages"], docs)
        result = st.chat_message("assistant").write_stream(response) # Output AI message
    st.session_state["messages"].append(AIMessage(result))           # Store AI message

