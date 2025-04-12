
import os

import streamlit as st
groq_api_key=os.getenv('GROQ_API_KEY')


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
model= ChatGroq(model='Llama3-8b-8192',groq_api_key=groq_api_key)

#langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']='Simple Q&A Chotbot'
#prompt template
prompt_template=ChatPromptTemplate.from_messages(
    
[('system',"you are helpful assistant. Please response to user queries"),
 ('user','Question :{question}')   
]    
)

def generate_response(question,api_key,llm,temperature,max_token):
    openai.api_key=api_key
    llm=ChatGroq(model=llm,groq_api_key=groq_api_key)
    out_parser=StrOutputParser()
    chain=prompt_template|llm|out_parser
    answer=chain.invoke({'question':question})
    return answer

st.title('Enhanced Q&A Chatbot With OpenAI')

# SIDEBARE FOR SETTING
st.sidebar.title('Settings')
api_key=st.sidebar.text_input('Enter Your OPEN AI API KEY',type='password')
## dropdown to select llm model

llm=st.sidebar.selectbox("select model",['llama3-70b-8192','llama3-8b-8192','gemma2-9b-it'])
temperature=st.sidebar.slider('Temperature',min_value=0.0,max_value=0.7,value=0.7)
max_token=st.sidebar.slider('Temperature',min_value=50,max_value=200,value=130)
st.write("Go ahead and ask any question ")
user_input= st.text_input('You:')
if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_token)
    st.write(response)
else:
    st.write("please provide query")






























