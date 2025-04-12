import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

# LangSmith (Optional)
os.environ['LANGCHAIN_API_KEY'] = st.secrets.get('LANGCHAIN_API_KEY', '')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = 'Simple Q&A Chatbot'

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful assistant. Please respond to user queries."),
    ('user', 'Question: {question}')
])

# Generate response
def generate_response(question, groq_key, llm_model, temperature, max_token):
    llm = ChatGroq(model=llm_model, groq_api_key=groq_key)
    out_parser = StrOutputParser()
    chain = prompt_template | llm | out_parser
    answer = chain.invoke({'question': question})
    return answer

# Streamlit UI
st.title('🧠 Enhanced Q&A Chatbot with Groq')

# Sidebar settings
st.sidebar.title('⚙️ Settings')

groq_api_key = st.secrets["GROQ_API_KEY"]
llm_model = st.sidebar.selectbox("Select Model", ['llama3-70b-8192', 'llama3-8b-8192', 'gemma2-9b-it'])
temperature = st.sidebar.slider('Temperature', min_value=0.0, max_value=0.7, value=0.7)
max_token = st.sidebar.slider('Max Tokens', min_value=50, max_value=200, value=130)

# Input
st.write("💬 Ask me anything:")
user_input = st.text_input('You:')

if user_input:
    response = generate_response(user_input, groq_api_key, llm_model, temperature, max_token)
    st.write(response)
else:
    st.write("👆 Enter your question above.")

